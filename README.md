# Flask Chatbot with API + Local Dataset

## Overview
A simple Flask-based chatbot that answers:
- Weather questions using a public API
- Movie-related queries using a local CSV dataset processed by a Python ETL pipeline

## Routes
- `POST /chat` — Send JSON: `{ "message": "your question" }`

## Setup 

1. Create a virtual environment and install dependencies:
   ```bash
     python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
   ```
2. Run ETL to prepare local data:
   ```bash
     python etl.py
   ```
3. Start the Flask app:
   ```bash
     python app.py
   ```
4. Access at public IP.

### Public URL 
http://34.57.73.18:5000/chat
