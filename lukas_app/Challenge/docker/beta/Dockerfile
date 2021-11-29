FROM alpine:latest

RUN apk add py3-flask

WORKDIR /app
ENTRYPOINT flask run --host=0.0.0.0 --port=80
ADD flag.txt /flag.txt
