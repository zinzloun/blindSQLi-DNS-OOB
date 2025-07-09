# ---------- web/Dockerfile ----------
FROM python:3.9-slim

# Install nslookup (via dnsutils o bind-tools)
RUN apt-get update && apt-get install -y dnsutils

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
