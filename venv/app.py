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

@app.route("/australia")
def australia():
    return "australia"

if __name__ == '__main__':
    app.run(debug=True)