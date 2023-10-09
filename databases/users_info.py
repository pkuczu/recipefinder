from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

# app = Flask(__name__, template_folder='group-project-team47/html')
app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Change this to a random secret key

conn = sqlite3.connect('users.db')
c = conn.cursor()
# c.execute('''
    # CREATE TABLE IF NOT EXISTS users (
        # id INTEGER PRIMARY KEY AUTOINCREMENT,
        # username TEXT NOT NULL,
        # password TEXT NOT NULL
    # )
# ''')
conn.commit()
conn.close()

# SQLite database file path
db_path = 'group-project-team47/databases/users.db'

@app.route('/')
def home():
    return render_template('/group-project-team47/html/registration-page.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if the username already exists
    '''cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        flash('Username already exists. Please choose a different username.', 'error')
        conn.close()
        return redirect(url_for('index'))'''

    # Insert new user into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    flash('Registration successful!', 'success')
    return redirect(url_for('webpage.html'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)
