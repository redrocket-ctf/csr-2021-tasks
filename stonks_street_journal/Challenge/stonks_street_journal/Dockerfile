FROM python

WORKDIR /opt
COPY ./requirements.txt /opt
RUN pip install -r requirements.txt
COPY . /opt
RUN mv stonks_street_journal/settings_production.py stonks_street_journal/settings.py
CMD sleep 10 && python manage.py migrate && gunicorn -b 0.0.0.0:8888 stonks_street_journal.wsgi
