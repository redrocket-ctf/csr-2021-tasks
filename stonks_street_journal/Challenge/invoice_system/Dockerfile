FROM python:3

WORKDIR /usr/src/app

RUN apt update && apt install -y netcat
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -U gunicorn
ADD app ./
CMD gunicorn -b 0.0.0.0:8000 -u gunicorn -g gunicorn wsgi:app -t 2 -w 8
