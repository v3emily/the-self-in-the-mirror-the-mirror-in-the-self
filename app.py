from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mirror():
    return render_template("mirror.html")

if __name__ == "__main__":
    app.run(debug=True)