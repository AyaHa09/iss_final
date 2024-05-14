from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@@36@%%7IZSoo",
    database="safelinkdb"
)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])  # Add "POST" to the methods parameter
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM policeOff WHERE email = %s AND passwordOfficer = %s", (email, password))
        officer = cursor.fetchone()

        if officer:
            return redirect(url_for("prisoners_dashboard")) 
        else:
            return render_template("login.html", message="Invalid email or password")  
    else:
        return redirect(url_for("login_page"))

@app.route("/prisoners_dashboard", methods=["POST"])
def prisoners_dashboard():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM prisoners")
    prisoners = cursor.fetchall()
    return render_template("prisoners_dashboard.html", prisoners=prisoners)

if __name__ == "__main__":
    app.run(debug=True)
