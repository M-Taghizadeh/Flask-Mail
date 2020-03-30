from flask import Flask, render_template, request
from flask_mail import Mail

app = Flask(__name__)
app.config.update(DEBUG=True, MAIL_SERVER='smtp.gmail.com',
                   MAIL_PORT=587, MAIL_USE_SSL=False, MAIL_USE_TLS=True, MAIL_USERNAME = 'taghizadeh.py@gmail.com', MAIL_PASSWORD="**********")
mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
def send_mail():
    sender = 'taghizadeh.py@gmail.com'
    recipients = ['taghizadeh.mhmd@gmail.com']
    if request.method == "POST":
        subject = request.form.get("subject")
        body = request.form.get("body")
        mail.send_message(sender=sender, recipients=recipients, subject=subject, body=body)
    return render_template("send_mail.html")
