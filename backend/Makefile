run:
	.venv\Scripts\activate && uvicorn app.main:app --reload --port 8000

install:
	.venv\Scripts\activate && pip install -r requirements.txt

lint:
	.venv\Scripts\activate && flake8 && black .

test:
	.venv\Scripts\activate && pytest