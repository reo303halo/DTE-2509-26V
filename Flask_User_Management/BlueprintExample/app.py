from flask import Flask, render_template
from flask_login import login_required, current_user
from database import DataBase
from routes.user_manager import users_bp, login_manager
from models.user import User
from models.car import Car
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
login_manager.init_app(app)



# Register the Blueprint
app.register_blueprint(users_bp, url_prefix='/users')

# Add more blueprints....


@app.route("/")
@login_required
def home():
    with DataBase() as db:
        cars = [Car(*car) for car in db.get_cars_by_owner(current_user.id)]

    return render_template('index.html', user = current_user, cars = cars)


if __name__ == '__main__':
    app.run(debug=True)
