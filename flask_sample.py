
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    # return "Welcome to Flask"
    return render_template('index.html')

@app.route("/LinearRegression", methods=['POST', 'GET'])
def linear():
    return render_template("linear_regression.html")


if __name__ == '__main__':
    app.run()