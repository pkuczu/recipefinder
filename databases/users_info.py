from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# SQLite database file path
db_path = 'group-project-team47/databases/users.db'

@app.route('/')
def index():
    return render_template('registration-page.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        flash('Username already exists. Please choose a different username.', 'error')
        conn.close()
        return redirect(url_for('index'))

    # Insert new user into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    flash('Registration successful!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
