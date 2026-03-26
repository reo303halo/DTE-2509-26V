from flask import Flask, render_template, redirect, url_for
from flask_wtf import CSRFProtect
from flask_login import LoginManager, logout_user, login_required, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

from database import DataBase
from user import User
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Redirects to login



@login_manager.user_loader
def load_user(user_id):
    with DataBase() as db:
        user = db.load_user(user_id)
    if user:
        return User(user[0], user[1], user[2], user[4])
    return None


@app.route("/")
@login_required
def home():
    return render_template('index.html', user=current_user)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        with DataBase() as db:
            db.create_user(
                form.name.data,
                form.email.data,
                generate_password_hash(form.password.data)
            )
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        with DataBase() as db:
            user = db.load_user_by_email(form.email.data)

            if user and check_password_hash(user[3], form.password.data):
                login_user(User(user[0], user[1], user[2], user[4]))
                return redirect(url_for("home"))

        return render_template("login.html", form=form, error="Invalid credentials")

    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))



if __name__ == '__main__':
    app.run(debug=True)