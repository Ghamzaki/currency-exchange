FROM python:3.10

WORKDIR /app

# Ensure apt is updated and python3-pip is installed
RUN apt-get update && apt-get install -y python3-pip

# Upgrade pip for best practices
RUN python3 -m pip install --upgrade pip

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY .

EXPOSE $PORT

CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]