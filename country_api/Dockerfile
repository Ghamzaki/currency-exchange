FROM python:3.10-slim-buster

WORKDIR /app

FROM ubuntu:latest

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3-pip

# Upgrade pip for best practices
RUN python3 -m pip install --upgrade pip

# Now proceed with your original steps
COPY requirements.txt .
#RUN pip install -r requirements.txt

# Or, use python3 to be explicit
RUN python3 -m pip install -r requirements.txt

COPY .

EXPOSE $PORT

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]