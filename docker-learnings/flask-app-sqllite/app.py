from flask import Flask, request, render_template_string, g
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "/app/data/users.db"

# Ensure data directory exists
os.makedirs("/app/data", exist_ok=True)

# Connect to database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
    return db

# Close DB connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()

init_db()

# HTML Template
template = """
<!doctype html>
<html>
<head>
    <title>Store Name & Age</title>
</head>
<body>
    <h1>Enter Details</h1>
    <form method="POST">
        Name: <input type="text" name="name"><br><br>
        Age: <input type="number" name="age"><br><br>
        <input type="submit" value="Submit">
    </form>

    <h2>Stored Entries:</h2>
    <ul>
    {% for entry in data %}
        <li>{{ entry[0] }} ({{ entry[1] }} years old)</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_db()
    c = conn.cursor()
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        if name and age:
            c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
            conn.commit()
    c.execute("SELECT name, age FROM users")
    rows = c.fetchall()
    return render_template_string(template, data=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

