from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route("/")  # @ --> route --> decorator
def index():  
    return render_template("index.html")

app.run(host="localhost", debug=True)

