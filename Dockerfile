FROM python:3.10-alpine

WORKDIR /app

COPY .env .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY extract/extract_ID.py ./extract_ID.py

CMD ["python", "extract_ID.py"]