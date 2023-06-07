FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev

WORKDIR /app
COPY . /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8888"]