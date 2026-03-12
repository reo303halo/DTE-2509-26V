from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash
import secrets

from save import saveToFile


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route('/') # GET
def home():
    return render_template("index.html")


@app.route('/sign_up') # GET
def sign_up():
    return render_template('signUp.html')


@app.route('/registration', methods = ["GET", "POST"])
def registration():

    if request.method == "POST":
        req = request.form

        firstname = req["firstname"]
        lastname = req["lastname"]
        email = req["email"]
        password = req["password"]
        confirm_password = req["confirm_password"]

        if password == confirm_password:
            saveToFile(firstname, lastname, email, generate_password_hash(password))

            flash("Registration complete!")
            flash("Welcome!")
            return render_template("index.html")
        
        else:
            flash("Password does not match!")
            return render_template("signUp.html")
        
    return redirect( url_for('home') )


if __name__ == '__main__':
    app.run(debug = True)