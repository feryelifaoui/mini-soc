import os
import streamlit as st

from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain

from pdf_generator import generate_pdf


# ---------------------------------------------------------------------------
# Configuration de la page
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Assistant Cybersécurité DDoS",
    page_icon="🛡️",
    layout="centered",
)


# ---------------------------------------------------------------------------
# Construction des composants (mise en cache pour ne pas recharger à chaque message)
# ---------------------------------------------------------------------------
@st.cache_resource(show_spinner="Chargement du modèle et de l'index FAISS...")
def build_components():
    from pathlib import Path
    current_dir = Path(__file__).resolve().parent
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.load_local(
        str(current_dir / "faiss_index"),
        embeddings,
        allow_dangerous_deserialization=True,
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatOllama(model="llama3", temperature=0.2)

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

    pdf_prompt = ChatPromptTemplate.from_template(
"""
Tu rédiges le contenu d'un document PDF professionnel de cybersécurité.

Règles strictes :
- Ne commence JAMAIS par une phrase comme "Voici", "D'accord", "Bien sûr", "Voilà"
- Ne termine JAMAIS par une phrase de conclusion de chat
- Réponds UNIQUEMENT avec le contenu du document, en markdown :
  - # pour le titre principal, ## pour les sous-titres
  - tableaux au format markdown standard : | Colonne1 | Colonne2 |
- Si une information manque dans le contexte, ignore-la simplement
- N'ajoute aucun commentaire sur ce que tu fais, uniquement le contenu final

Contexte :
{context}

Sujet du document :
{input}

Contenu du document (markdown pur, sans aucune phrase de chat) :
"""
    )

    chat_document_chain = create_stuff_documents_chain(llm, chat_prompt)
    chat_chain = create_retrieval_chain(retriever, chat_document_chain)

    pdf_document_chain = create_stuff_documents_chain(llm, pdf_prompt)

    return {
        "chat_chain": chat_chain,
        "pdf_document_chain": pdf_document_chain,
    }


# ---------------------------------------------------------------------------
# État de session
# ---------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []  # liste de {"role": "user"/"assistant", "content": str}

if "last_context" not in st.session_state:
    st.session_state.last_context = None  # documents FAISS de la dernière question

if "last_question" not in st.session_state:
    st.session_state.last_question = None

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = None


# ---------------------------------------------------------------------------
# En-tête
# ---------------------------------------------------------------------------
st.title("🛡️ Assistant Cybersécurité — DDoS / DoS")
st.caption("Chatbot RAG basé sur tes documents locaux (FAISS + Ollama)")

components = build_components()
chat_chain = components["chat_chain"]
pdf_document_chain = components["pdf_document_chain"]


# ---------------------------------------------------------------------------
# Affichage de l'historique de conversation
# ---------------------------------------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ---------------------------------------------------------------------------
# Zone de saisie du chat
# ---------------------------------------------------------------------------
question = st.chat_input("Pose ta question sur le DoS / DDoS...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Recherche dans les documents..."):
            response = chat_chain.invoke({"input": question})
            answer = response["answer"]
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.session_state.last_context = response["context"]
    st.session_state.last_question = question
    st.session_state.pdf_path = None  # on invalide l'ancien PDF tant qu'un nouveau n'est pas généré


# ---------------------------------------------------------------------------
# Génération de PDF (bouton séparé, indépendant du chat_input)
# ---------------------------------------------------------------------------
st.divider()
st.subheader("📄 Générer un rapport PDF")

col1, col2 = st.columns([3, 1])
with col1:
    pdf_subject = st.text_input(
        "Sujet du PDF",
        value=st.session_state.last_question or "Tableau comparatif DoS vs DDoS",
        label_visibility="collapsed",
        placeholder="Sujet du PDF (ex : Tableau comparatif DoS vs DDoS)",
    )
with col2:
    generate_clicked = st.button("Générer le PDF", use_container_width=True)

if generate_clicked:
    if st.session_state.last_context is None:
        # Pas encore de contexte récupéré : on fait une recherche dédiée pour ce sujet
        with st.spinner("Recherche du contexte pertinent..."):
            temp_response = chat_chain.invoke({"input": pdf_subject})
            context_to_use = temp_response["context"]
    else:
        context_to_use = st.session_state.last_context

    with st.spinner("Génération du contenu et du PDF..."):
        pdf_content = pdf_document_chain.invoke({
            "input": pdf_subject,
            "context": context_to_use,
        })
        output_path = os.path.join(os.getcwd(), "ddos_report.pdf")
        generate_pdf(pdf_content, output_path)
        st.session_state.pdf_path = output_path

    st.success("PDF généré avec succès !")

if st.session_state.pdf_path and os.path.exists(st.session_state.pdf_path):
    with open(st.session_state.pdf_path, "rb") as f:
        st.download_button(
            label="⬇️ Télécharger le PDF",
            data=f.read(),
            file_name="ddos_report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )


# ---------------------------------------------------------------------------
# Barre latérale : réinitialisation
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("Options")
    if st.button("🗑️ Réinitialiser la conversation"):
        st.session_state.messages = []
        st.session_state.last_context = None
        st.session_state.last_question = None
        st.session_state.pdf_path = None
        st.rerun()