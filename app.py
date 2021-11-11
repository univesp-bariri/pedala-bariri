from flask import Flask, render_template, redirect, request, flash, url_for
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
import os, datetime
import sqlite3
from werkzeug.exceptions import abort
from datetime import datetime 

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'itsok'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class Postsgastro(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.String(20), default=datetime.strftime(datetime.now(), '%d/%m/%Y'))
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(200), nullable=False)

class Postscultural(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.String(20), default=datetime.strftime(datetime.now(), '%d/%m/%Y'))
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(200), nullable=False)

class Postsrural(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.String(20), default=datetime.strftime(datetime.now(), '%d/%m/%Y'))
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(200), nullable=False)

email_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'MAIL_USERNAME',
    "MAIL_PASSWORD": 'MAIL_PASSWORD'
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

@app.route('/gastronomica')
def gastro():
    postsgastro = Postsgastro.query.order_by(Postsgastro.id.desc())
    return render_template('gastronomica.html', postsgastro=postsgastro)

@app.route('/cultural')
def cultural():
    postscultural = Postscultural.query.order_by(Postscultural.id.desc())
    return render_template('cultural.html', postscultural=postscultural)

@app.route('/rural')
def rural():
    postsrural = Postsrural.query.order_by(Postsrural.id.desc())
    return render_template('rural.html', postsrural=postsrural)


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

@app.route('/create-gastro', methods=['POST'])
def createGastro():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash("Insira seu nome!")
        else:
            postsgastro = Postsgastro(title=title, content=content)
            db.session.add(postsgastro)
            db.session.commit()
            return redirect(url_for('gastro'))
    return render_template('gastronomica.html')

@app.route('/create-cultural', methods=['POST'])
def createCultural():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash("Insira seu nome!")
        else:
            postscultural = Postscultural(title=title, content=content)
            db.session.add(postscultural)
            db.session.commit()
            return redirect(url_for('cultural'))
    return render_template('cultural.html')

@app.route('/create-rural', methods=['POST'])
def createRural():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash("Insira seu nome!")
        else:
            postsrural = Postsrural(title=title, content=content)
            db.session.add(postsrural)
            db.session.commit()
            return redirect(url_for('rural'))
    return render_template('rural.html')

if __name__ == '__main__':
    app.run(debug=True)