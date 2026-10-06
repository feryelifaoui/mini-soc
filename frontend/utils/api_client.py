import requests
import logging

BASE_URL = "http://localhost:8000/api/v1"
logger = logging.getLogger("api_client")


def predict_flow(features: dict) -> dict:
    try:
        r = requests.post(f"{BASE_URL}/predict", json=features, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def agent_analyze(features: dict) -> dict:
    try:
        r = requests.post(f"{BASE_URL}/agent/analyze", json=features, timeout=300)
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def rag_chat(question: str) -> dict:
    try:
        r = requests.post(f"{BASE_URL}/rag/chat", json={"question": question}, timeout=300)
        return r.json()
    except Exception as e:
        return {"answer": f"Service RAG indisponible : {e}", "status": "error"}


def get_dashboard_stats() -> dict:
    try:
        r = requests.get(f"{BASE_URL}/dashboard/stats", timeout=15)
        return r.json()
    except Exception as e:
        return {"total_incidents": 0, "total_tickets": 0, "avg_confidence": 0.0, "status_distribution": {}}


def get_incidents(limit: int = 50) -> list:
    try:
        r = requests.get(f"{BASE_URL}/dashboard/incidents", params={"limit": limit}, timeout=15)
        return r.json().get("incidents", [])
    except Exception as e:
        return []


def get_tickets(limit: int = 50) -> list:
    try:
        r = requests.get(f"{BASE_URL}/dashboard/tickets", params={"limit": limit}, timeout=15)
        return r.json().get("tickets", [])
    except Exception as e:
        return []


def update_incident_status(incident_id: int, status: str) -> dict:
    try:
        r = requests.put(f"{BASE_URL}/dashboard/incidents/{incident_id}/status", json={"status": status}, timeout=15)
        return r.json()
    except Exception as e:
        return {"error": str(e), "status": "error"}

