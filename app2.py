from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template("index.html")

@app.route("/cat")
def ddd():
    return 'sfsdfdf'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)