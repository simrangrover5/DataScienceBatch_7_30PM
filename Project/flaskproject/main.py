from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route("/")  # @ --> route --> decorator
def index():  
    return render_template("index.html")

@app.route("/filterjob/")
def filterjob():
    return render_template("jobform.html")

app.run(host="localhost", debug=True)

