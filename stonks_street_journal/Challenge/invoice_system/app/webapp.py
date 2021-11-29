from flask import redirect, Flask, render_template, request, abort
from flask import url_for, send_from_directory, make_response, Response
import psycopg2
import base64
import datetime


app = Flask(__name__)

@app.route('/legacy_invoice_system/<string:encoded_user>')
def invoice(encoded_user):
    dec = base64.urlsafe_b64decode(encoded_user).decode()
    user, date = dec.split("-", 1)
    
    # TODOs:
    # check values for quotes. respond with IDS message.
    # fix links in template
    # add articles
    
    try:
        conn = psycopg2.connect("dbname='postgres' user='invoice' host='db'")
        cur = conn.cursor()
        cur.execute(f"""SELECT * from public.news_subscriber WHERE username='{user}' AND signup_date='{date}'""")
        rows = cur.fetchall()
        # (35, 'xxx', 'xxx', 123, 'rugo+dns@mailbox.org', '1111 1111 1111 1111', datetime.date(2021, 5, 27))
        if rows:
            id, uname, pw, pensi, email, credit_card, signup_date = rows[0]
            return render_template(
                'base.html', 
                username=uname,
                pensi=pensi,
                email=email,
                credit_card=credit_card,
                signup_date=signup_date
                )
        else:
            return "Error"
    except Exception as ex:
        return str(ex)


if __name__ == '__main__':
    app.run()

