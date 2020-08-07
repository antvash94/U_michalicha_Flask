from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)
password = '#'
s_email = '#'


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/form', methods=['POST'])
def form():
    name = request.form.get('name')
    message = request.form.get('message')
    email = request.form.get('email')
    text = 'Welcome'
    info = f'{message},{email},{name}'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(s_email, password)
    server.sendmail(s_email, email, text)
    server.sendmail(s_email, s_email, info)

    if not name or not message or not email:
        error_statement = 'All form fields required...'
        return render_template('index.html', error_statement=error_statement)
    return render_template('title.html', name=name, email=email, message=message)



if __name__ == "__main__":
    app.run()
