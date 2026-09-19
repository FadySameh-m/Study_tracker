# Study Tracker

#### Video Demo: [https://youtu.be/BYEsWqVT6s0]

#### Description:

Study Tracker is a web-based application designed to help students keep track of their study sessions. The application allows users to create an account, log in securely, record the amount of time they spend studying different subjects, add notes about each study session, and view statistics about their overall study time.

The main goal of Study Tracker is to provide a simple way for students to organize and monitor their study habits. Instead of keeping study records manually, users can store their sessions in a database and view them later from their personal dashboard.

The application is built using Python and Flask for the backend, SQLite for storing data, HTML for the structure of the web pages, and CSS for the visual design.

The application starts with a login page. Users who do not have an account can create one through the registration page. During registration, the application checks that all required fields have been provided and that the password confirmation matches the password. It also checks whether the chosen username already exists. Passwords are not stored as plain text. Instead, they are hashed using Werkzeug's password hashing functions before being stored in the database.

After logging in, the user is taken to the dashboard. The dashboard displays all study sessions belonging to the currently logged-in user. Each session contains the subject studied, the number of minutes spent studying, the date of the session, and optional notes.

The dashboard also calculates and displays statistics for the user's study activity. It shows the total number of study sessions and the total amount of study time. The total number of minutes is converted into hours and remaining minutes to make the information easier to understand.

Users can add a new study session through the Add Study Session page. The form asks for the subject, number of minutes, date, and optional notes. When the form is submitted, the new session is stored in the SQLite database and associated with the currently logged-in user.

Users can also delete their study sessions. The application checks the session ID together with the logged-in user's ID when deleting a record. This prevents a user from deleting a study session belonging to another user.

The application uses Flask sessions to keep track of the currently logged-in user. Routes that require authentication check whether a user ID exists in the session before allowing access. Users can also log out, which clears the session.

The main application logic is contained in app.py. This file creates the Flask application, connects to the SQLite database, defines the routes, handles registration and login, manages study sessions, calculates statistics, and handles logout.

The templates folder contains the HTML templates used by Flask. layout.html provides the common page structure and navigation. index.html contains the dashboard and displays the user's study sessions and statistics. add.html contains the form used to create a study session. login.html contains the login form, while register.html contains the account creation form.

The static folder contains style.css, which controls the visual appearance of the application. It defines the page layout, navigation bar, forms, buttons, tables, colors, spacing, and other visual elements.

The tracker.db file is the SQLite database used by the application. It stores user accounts and study sessions. Study sessions are associated with users so that each user can access only their own study records.

I chose Flask because it provides a simple way to connect Python code with HTML templates and handle web requests. I chose SQLite because the project does not require a large database system and SQLite is simple to use while still allowing the application to store structured data persistently.

The project combines several of the technologies and concepts learned throughout CS50x, including Python, SQL, Flask, HTML, CSS, databases, authentication, sessions, and web application development.

## Features
User registration and login
Password hashing
Add and delete study sessions
Track total study time
SQLite database
Responsive web interface

## Technologies
Python
Flask
SQLite
CS50 SQL
HTML
CSS
Jinja2
