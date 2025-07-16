FROM python:3.14.0a1-alpine3.20

# Установка glibc и необходимых утилит
RUN apk update && \
    apk add --no-cache bash curl wget ca-certificates && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk && \
    apk add glibc-2.30-r0.apk && \
    rm glibc-2.30-r0.apk

WORKDIR /usr/workspace

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Установка Playwright и всех браузеров
RUN pip install playwright && playwright install --with-deps

# (Опционально) Установка allure-pytest
RUN pip install allure-pytest

COPY . .

CMD ["pytest", "--alluredir=result"] 