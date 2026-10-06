import logging
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
logger = logging.getLogger("router.rag")


class RAGQuery(BaseModel):
    question: str


@router.post("/rag/chat", summary="Chatbot RAG Cybersécurité")
def rag_chat(query: RAGQuery):
    """
    Répond à une question de cybersécurité via le système RAG (LangChain + FAISS + Ollama).
    """
    try:
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "chatbot-rag"))
        from chatbot import build_components
        components = build_components()
        chat_chain = components["chat_chain"]
        result = chat_chain.invoke({"input": query.question})
        return {
            "question": query.question,
            "answer": result["answer"],
            "status": "success"
        }
    except Exception as e:
        logger.warning(f"RAG non disponible : {e}")
        return {
            "question": query.question,
            "answer": (
                "Le service RAG est actuellement indisponible (Ollama non démarré). "
                "Conseil général : Une attaque DDoS inonde le serveur de requêtes pour le rendre inaccessible. "
                "Recommandations : Bloquer les IPs sources, activer les règles anti-DDoS du firewall, "
                "mettre en place un rate-limiting et contacter votre fournisseur de services pour filtrage en amont."
            ),
            "status": "fallback"
        }
