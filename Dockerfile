FROM python:3.10-alpine as base
WORKDIR /app/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add --update --virtual .build-deps \
    build-base \
    python3-dev \
    libpq \
    gcc \
    libffi-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.10-alpine
WORKDIR /app/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /app:$PYTHONPATH

RUN apk add --update --no-cache libpq gettext

COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/

COPY ./start.dev.sh .

RUN chmod +x ./start.dev.sh && dos2unix ./start.dev.sh

COPY telegram_bot/ ./telegram_bot/
