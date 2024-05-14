from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import serial
import pynmea2

app = Flask(__name__)
app.secret_key = "your_secret_key"

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@@36@%%IZSoo",  
    database="safelinkdb"
)



@app.route("/update_gps")
def update_gps():
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    newdata = ser.readline().decode('latin-1')

    if newdata.startswith("$GPRMC"):
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        lng = newmsg.longitude

       
        cursor = mydb.cursor()
        cursor.execute("UPDATE prisoners SET latitude = %s, longitude = %s", (lat, lng))
        mydb.commit()
        return "GPS coordinates updated successfully", 200
    else:
        return "No GPS data found", 404

if __name__ == "__main__":
    app.run(debug=True)
