from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@@36@%%7IZSoo",
    database="safelinkdb"
)

@app.route("/prisoners")
def get_prisoners():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM prisoners")
    prisoners = cursor.fetchall()
    return jsonify(prisoners)

@app.route("/prisoners_dashboard")
def prisoners_dashboard():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM prisoners")
    prisoners = cursor.fetchall()
    return render_template("prisoners_dashboard.html", prisoners=prisoners)

if __name__ == "__main__":
    app.run(debug=True)
