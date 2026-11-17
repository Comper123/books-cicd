FROM python:3.11.10-slim

WORKDIR /app

COPY books.py .
COPY app.py .
COPY books.json.example .

CMD ["python", "app.py", "books.json.example", "--authot", "пушкин"]
