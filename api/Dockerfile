FROM python:alpine

RUN mkdir -p /app
WORKDIR /app

# RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev zlib libffi-dev cargo jpeg-dev zlib-dev
# RUN apk add --no-cache --virtual .build-deps build-base linux-headers libxslt-dev libxml2-dev

# RUN pip install --upgrade pip && hash -r && pip install --upgrade poetry

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]