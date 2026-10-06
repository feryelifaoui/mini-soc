# Mini SOC Intelligent

Mini SOC Intelligent is an AI-powered Security Operations Center (SOC) system consisting of a FastAPI backend and a Streamlit frontend. It includes features such as Machine Learning integration, a RAG-based Chatbot, and database management.

## Project Structure

- `backend/`: FastAPI application acting as the core API.
- `frontend/`: Streamlit web interface for users.
- `chatbot-rag/`: Retrieval-Augmented Generation chatbot functionalities.
- `database/`: Database configuration and utilities.
- `modele ml/`: Machine Learning models and scripts.
- `*.pdf`: Example incident reports.

## Setup & Run

A convenience script is provided for Windows users to quickly start the required services.

1. Install dependencies (if setting up from scratch):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run the application:
   Double click the `start_mini_soc.bat` file, or run it from the command line:
   ```bash
   .\start_mini_soc.bat
   ```

This will launch:
- The Streamlit Frontend at `http://localhost:8501`
- The FastAPI Backend at `http://localhost:8000`
- API Documentation at `http://localhost:8000/docs`
