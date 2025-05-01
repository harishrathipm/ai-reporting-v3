run:
	.venv\Scripts\activate && uvicorn main:app --reload

install:
	.venv\Scripts\activate && pip install -r requirements.txt

lint:
	.venv\Scripts\activate && flake8 && black .

test:
	.venv\Scripts\activate && pytest