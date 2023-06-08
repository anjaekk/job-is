FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    default-libmysqlclient-dev

RUN pip install --upgrade pip
RUN pip install poetry

ENV PATH=/root/.local/bin:$PATH

COPY . /app

WORKDIR /app

ENV VIRTUAL_ENV=/opt/env
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN poetry install --no-root 

EXPOSE 8888

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8888"]