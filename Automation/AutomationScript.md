We will start our project in python by importing the important features we need like Flask,datetime, and random


<img width="388" alt="12" src="https://github.com/23W-GBAC/MohAli92/assets/148862863/6d6e6be1-989c-495f-9809-f4c9a557079d">

from flask import Flask, render_template: This imports the Flask class from the Flask module, which allows us to create a Flask web application. render_template is a function provided by Flask for rendering HTML templates.
import datetime: Imports the datetime module, which provides classes for manipulating dates and times.
import random: Imports the random module, which provides functions for generating random numbers.


<img width="382" alt="13" src="https://github.com/23W-GBAC/MohAli92/assets/148862863/ef1b7223-3e91-4313-b79b-7d96f083ceea">

app = Flask(__name__): This creates a Flask application instance. __name__ is a special variable in Python that represents the name of the current module. When this script is executed, __name__ will be '__main__', indicating that this module is being run as the main program.


<img width="482" alt="14" src="https://github.com/23W-GBAC/MohAli92/assets/148862863/a768c2bd-b653-4aa0-bcc4-badd50c76c71">

AppointmentReminder: This is a custom class representing an appointment reminder. It has three attributes: patient_name, appointment_datetime, and contact_number. It also has a method called send_reminder() which generates a reminder message.


<img width="485" alt="15" src="https://github.com/23W-GBAC/MohAli92/assets/148862863/c6e6a8f7-1f1f-44aa-8fee-3511a5d286c7">

generate_random_datetime(): This function generates a random datetime within the next 7 days from the current datetime.


<img width="479" alt="16" src="https://github.com/23W-GBAC/MohAli92/assets/148862863/f9ae8900-651c-4c25-a72b-77d551be9860">

<img width="479" alt="16a" src="https://github.com/23W-GBAC/MohAli92/assets/148862863/50f7e8b7-14e9-40ab-9f66-cc296d614fc3">

@app.route('/'): This is a decorator that associates the index function with the root URL of the Flask application.
index(): This function retrieves a list of appointments, generates random datetimes for each appointment, creates AppointmentReminder objects, sends reminders, and stores them in a list.
render_template('index.html', reminders=reminders): This function renders an HTML template called index.html, passing the list of reminders to it.


<img width="481" alt="17" src="https://github.com/23W-GBAC/MohAli92/assets/148862863/9ef3bc3c-326c-49a9-9fa5-713c0be2f4bf"><img width="481" alt="17" src="https://github.com/23W-GBAC/MohAli92/assets/148862863/9ef3bc3c-326c-49a9-9fa5-713c0be2f4bf">

if __name__ == '__main__':: This block of code ensures that the Flask application only runs if this script is executed directly (not imported as a module).
app.run(debug=True): This command starts the Flask development server. Setting debug=True enables debug mode, which provides helpful debugging information in case of errors.
