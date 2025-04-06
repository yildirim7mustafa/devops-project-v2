python3 -m venv venv
source venv/bin/activate
pip install fastapi[all]
fastapi dev main.py
uvicorn app.main:app --reload