from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message='Email is required.'), Email('Email must contain @.')])
    password = PasswordField(label='Password', validators=[DataRequired(message='Password is required.'), Length(min=8, max=16, message='Password must between 8 and 16 characters.')])
    submit = SubmitField(label='Log In')


def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app
  
app = create_app()
app.secret_key = "hehe"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:    
            return render_template('denied.html', form=login_form)
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)