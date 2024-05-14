import serial

import time

import string

import pynmea2



while True:

    port = "/dev/ttyAMA0"

    ser = serial.Serial(port, baudrate=9600, timeout=0.5)

    dataout = pynmea2.NMEAStreamReader()



    # Read bytes from the serial port

    newdata = ser.readline()



    # Decode the bytes using 'latin-1' encoding

    newdata_decoded = newdata.decode('latin-1')



    if newdata_decoded.startswith("$GPRMC"):

        newmsg = pynmea2.parse(newdata_decoded)

        lat = newmsg.latitude

        lng = newmsg.longitude

        gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)

        print(gps)

