from flask import Flask, render_template, redirect, request, flash
import smtplib
from flask_mail import Mail, Message

app = Flask('__name__')
app.secret_key = "itsok"

email_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": GMAIL_USER,
    "MAIL_PASSWORD": GMAIL_PASSWORD
}

app.config.update(email_settings)
mail = Mail(app)

class Contato:
    def __init__(self,nome,email,mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message(
            subject = f'{formContato.nome} enviou uma mensagem',
            sender = app.config.get("MAIL_USERNAME"),
            recipients = [app.config.get("MAIL_USERNAME")],
            body = f'''
            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:

            {formContato.mensagem}

            '''
        )

        mail.send(msg)
        flash("Mensagem enviada com sucesso!")
    
    return redirect('/')

if __name__ == '__mainn__':
    app.run(debug=True)
