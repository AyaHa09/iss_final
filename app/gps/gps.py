import serial
import pynmea2
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="safelinkdb"
)

def update_database_with_gps():
    while True:
        port = "/dev/ttyAMA0"
        ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        
       
        newdata = ser.readline().decode('latin-1')

        if newdata.startswith("$GPRMC"):
            newmsg = pynmea2.parse(newdata)
            lat = newmsg.latitude
            lng = newmsg.longitude

            
            cursor = mydb.cursor()
            sql = "INSERT INTO prisoners (latitude, longitude) VALUES (%s, %s)"
            val = (lat, lng)
            cursor.execute(sql, val)
            mydb.commit()

            print("Latitude:", lat, "Longitude:", lng)

if __name__ == "__main__":
    update_database_with_gps()
