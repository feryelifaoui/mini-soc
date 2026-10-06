@echo off
echo ============================================================
echo     MINI SOC INTELLIGENT — DEMARRAGE DES SERVICES
echo ============================================================
echo.

cd /d "%~dp0"
set PYTHONUTF8=1

echo [1/2] Demarrage du Backend FastAPI (port 8000)...
start "Mini SOC - FastAPI Backend" cmd /k "cd /d "%~dp0" && call venv\Scripts\activate && python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload"

timeout /t 4 /nobreak >nul

echo [2/2] Demarrage du Frontend Streamlit (port 8501)...
start "Mini SOC - Streamlit UI" cmd /k "cd /d "%~dp0" && call venv\Scripts\activate && python -m streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0"

echo.
echo ============================================================
echo  Services demarres !
echo  - Backend API  : http://localhost:8000
echo  - Docs API     : http://localhost:8000/docs
echo  - Interface UI : http://localhost:8501
echo ============================================================
echo.
echo NOTE : Pour les alertes email, configurez SMTP_PASSWORD dans
echo        backend/config.py ou via variable d'environnement
echo        SMTP_PASSWORD=votre_mot_de_passe_app_gmail
echo.
pause
