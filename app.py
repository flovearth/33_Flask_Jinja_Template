from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1 = 12, number2 = 34)

@app.route("/about")
def second():
    return render_template("about.html", hazirlayan = "Feyzullah SARI")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug = True)
