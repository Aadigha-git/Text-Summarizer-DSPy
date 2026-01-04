FROM python:3.8-slim-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y \
    awscli \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Upgrade pip (optional but recommended)
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir transformers accelerate

CMD ["python", "app.py"]
