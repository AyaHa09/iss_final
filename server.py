from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key"
bcrypt = Bcrypt(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@@36@%%7IZSoo@localhost/safelinkdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your model
class PoliceOff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Prisoners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

# Routes
@app.route("/")
def login_page():
    return render_template("login.html", message="")



@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        officer = PoliceOff.query.filter_by(email=email).first()

        if officer and bcrypt.check_password_hash(officer.password, password):
            session["email"] = email
            return redirect(url_for("prisoners_dashboard"))
        else:
            return render_template("login.html", message="Invalid email or password")
        
@app.route("/prisoners_dashboard")
def prisoners_dashboard():
    if "email" in session:
        prisoners = Prisoners.query.all()
        return render_template("prisoners_dashboard.html", prisoners=prisoners)
    else:
       
        return redirect(url_for("login_page"))

if __name__ == "__main__":
    app.run(debug=True)