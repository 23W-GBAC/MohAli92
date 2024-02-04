from flask import Flask, render_template
import datetime
import random

app = Flask(__name__)

class AppointmentReminder:
    def __init__(self, patient_name, appointment_datetime, contact_number):
        self.patient_name = patient_name
        self.appointment_datetime = appointment_datetime
        self.contact_number = contact_number

    def send_reminder(self):
        # In a real-world scenario, you would integrate with a messaging service API here
        # For simplicity, let's simulate sending a reminder
        reminder_message = f"Hi {self.patient_name}! Your appointment is scheduled for {self.appointment_datetime}."
        return reminder_message

def generate_random_datetime():
    # Generate a random datetime within the next 7 days
    current_datetime = datetime.datetime.now()
    random_days = random.randint(1, 7)
    appointment_datetime = current_datetime + datetime.timedelta(days=random_days)
    return appointment_datetime

@app.route('/')
def index():
    # Assume you have a list of appointments with patient information
    appointments = [
        {"patient_name": "Moh_Nouh", "contact_number": "+1234567890"},
        {"patient_name": "Ali_Ahmed", "contact_number": "+9876543210"},
        # Add more appointments as needed
    ]

    reminders = []

    for appointment in appointments:
        # For simplicity, let's generate a random datetime for each appointment
        appointment_datetime = generate_random_datetime()

        # Create an AppointmentReminder object
        reminder = AppointmentReminder(
            patient_name=appointment["patient_name"],
            appointment_datetime=appointment_datetime,
            contact_number=appointment["contact_number"]
        )

        # Send the reminder and store it in the list
        reminders.append(reminder.send_reminder())

    return render_template('index.html', reminders=reminders)

if __name__ == '__main__':
    app.run(debug=True)
