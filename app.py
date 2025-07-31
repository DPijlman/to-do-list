from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Placeholder empty tasks array
tasks = []

@app.route("/")
def home():
    # This makes the app use the index.html file
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]
    tasks.append(task)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)