"""
Point d'entrée pour lancer l'API DDoS Detection.
Usage : python run.py
"""
import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    print("=" * 60)
    print("  🛡️  DDoS Detection API — Mini-SOC")
    print("=" * 60)
    print(f"  📍 URL  : http://{settings.API_HOST}:{settings.API_PORT}")
    print(f"  📖 Docs : http://localhost:{settings.API_PORT}/docs")
    print(f"  📋 ReDoc: http://localhost:{settings.API_PORT}/redoc")
    print("=" * 60)

    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD,
        log_level="info",
    )
