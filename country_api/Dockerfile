FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY .

EXPOSE $PORT

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]