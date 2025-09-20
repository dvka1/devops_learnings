from flask import Flask, request, render_template_string

app = Flask(__name__)

# In-memory storage (reset when container restarts)
data = []

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
        <li>{{ entry['name'] }} ({{ entry['age'] }} years old)</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        if name and age:
            data.append({"name": name, "age": age})
    return render_template_string(template, data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

