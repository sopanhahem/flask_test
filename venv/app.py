from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/sopanha")
def sopanha():
    return "hello Cambodia"

@app.route("/tasmania")
def tasmania():
    return "tasmania"

if __name__ == '__main__':
    app.run(debug=True)