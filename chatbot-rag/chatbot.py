# chatbot.py — lance le chatbot en ligne de commande

from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
try:
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain.chains import create_retrieval_chain
except ModuleNotFoundError:
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain
    from langchain_classic.chains import create_retrieval_chain

from functools import lru_cache

from pdf_generator import generate_pdf


@lru_cache(maxsize=1)
def build_components():
    """Initialise et retourne les composants réutilisables : llm, retriever, chaînes."""

    # 1. Charger l'index vectoriel FAISS
    from pathlib import Path
    current_dir = Path(__file__).resolve().parent
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.load_local(
        str(current_dir / "faiss_index"),
        embeddings,
        allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    # 2. Configurer le LLM
    llm = ChatOllama(model="llama3", temperature=0.2)

    # 3. Prompt pour le CHAT (réponse conversationnelle normale)
    chat_prompt = ChatPromptTemplate.from_template(
"""
Tu es un assistant spécialisé en cybersécurité.
Réponds uniquement avec les informations présentes dans le contexte.
Si l'information n'existe pas dans le contexte, dis :
"Je ne trouve pas cette information dans mes documents."

Contexte :
{context}

Question :
{input}

Réponse :
"""
    )

    # 4. Prompt pour la GÉNÉRATION DE PDF (contenu de document, pas de phrases de chat)
    pdf_prompt = ChatPromptTemplate.from_template(
"""
Tu rédiges le contenu d'un document PDF professionnel de cybersécurité.

Règles strictes :
- Ne commence JAMAIS par une phrase comme "Voici", "D'accord", "Bien sûr", "Voilà"
- Ne termine JAMAIS par une phrase de conclusion de chat comme "Je ne trouverai pas d'autres informations"
- Réponds UNIQUEMENT avec le contenu du document, en markdown :
  - Utilise # pour le titre principal, ## pour les sous-titres
  - Utilise le format markdown standard pour les tableaux : | Colonne1 | Colonne2 |
- Si une information manque dans le contexte, ignore-la simplement, ne le mentionne pas
- N'ajoute aucun commentaire sur ce que tu fais, uniquement le contenu final

Contexte :
{context}

Sujet du document :
{input}

Contenu du document (markdown pur, sans aucune phrase de chat) :
"""
    )

    # 5. Créer les deux chaînes RAG (chat + pdf), qui partagent le même retriever
    chat_document_chain = create_stuff_documents_chain(llm, chat_prompt)
    chat_chain = create_retrieval_chain(retriever, chat_document_chain)

    pdf_document_chain = create_stuff_documents_chain(llm, pdf_prompt)

    return {
        "llm": llm,
        "retriever": retriever,
        "chat_chain": chat_chain,
        "pdf_document_chain": pdf_document_chain,
    }


def main():
    print("Chargement du chatbot RAG... (patiente quelques secondes)")
    components = build_components()
    chat_chain = components["chat_chain"]
    pdf_document_chain = components["pdf_document_chain"]

    print("Chatbot prêt ! Tape 'exit' pour quitter.\n")

    while True:
        question = input("Toi : ")
        if question.lower() in ["exit", "quit", "q"]:
            print("À bientôt !")
            break

        # Appel du RAG conversationnel
        response = chat_chain.invoke({"input": question})
        answer = response["answer"]

        print("\nAssistant :")
        print(answer)
        print()

        # Génération PDF si demandé
        if "pdf" in question.lower():
            # Réutilise les documents déjà récupérés par chat_chain pour ne pas
            # relancer une recherche FAISS inutilement
            retrieved_docs = response["context"]

            pdf_content = pdf_document_chain.invoke({
                "input": question,
                "context": retrieved_docs
            })

            pdf_file = generate_pdf(pdf_content, "ddos_report.pdf")
            print(f"PDF généré : {pdf_file}")
            print()


if __name__ == "__main__":
    main()