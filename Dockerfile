# syntax=docker/dockerfile:1

FROM python:3.9-alpine

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "llm.main:app", "host:0.0.0.0"]