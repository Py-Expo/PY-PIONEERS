from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(_name_)

# Function to connect to SQLite database
def connect_db():
    return sqlite3.connect('database.db')

# Route for rendering the login form
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the login form submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Connect to the database
    conn = connect_db()
    cursor = conn.cursor()

    # Query the database to check if the username and password match
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    # Close the database connection
    conn.close()

    if user:
        # Redirect to some other page on successful login
        return redirect(url_for('success'))
    else:
        # Redirect back to the login page if login fails
        return redirect(url_for('index'))

# Route for the page to redirect after successful login
@app.route('/success')
def success():
    return "Login successful!"

if _name_ == '_main_':
    app.run(debug=True)