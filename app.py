from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rutujazankar@31",
    database="adv_parking_sys"
)

cursor = db.cursor(dictionary=True)

# -------- SAVE BOOKING DATA --------
@app.route("/save-booking", methods=["POST"])
def save_booking():
    name = request.form.get("name")
    mobile = request.form.get("mobile")
    vehicle = request.form.get("vehicle")
    mh = request.form.get("mh")

    now = datetime.now()

    cursor.execute("""
        INSERT INTO parking_bookings
        (name, mobile, vehicle_type, mh_number, booking_datetime)
        VALUES (%s,%s,%s,%s,%s)
    """, (name, mobile, vehicle, mh, now))

    db.commit()
    return "Saved Successfully"

# -------- SHOW BOOKING DATA --------
@app.route("/bookings")
def bookings():
    cursor.execute("SELECT * FROM parking_bookings")
    data = cursor.fetchall()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
