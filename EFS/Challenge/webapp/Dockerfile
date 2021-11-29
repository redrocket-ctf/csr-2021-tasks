FROM python:3

WORKDIR /usr/src/app

COPY flag.txt /
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ADD app ./
RUN mkdir /tmp/uploads && chmod 333 /tmp/uploads
RUN useradd -U gunicorn
CMD gunicorn -b 0.0.0.0:8000 -u gunicorn -g gunicorn wsgi:app --error-logfile "-" -t 5 
