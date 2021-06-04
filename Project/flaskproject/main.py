from flask import Flask, render_template, request, redirect, url_for
from df import get_jobtitle, get_keyskills, get_location
import pandas as pd
import numpy as np

app = Flask(__name__) 

@app.route("/")  # @ --> route --> decorator
def index():  
    return render_template("index.html")

@app.route("/filterjob/")
def filterjob():
    title = get_jobtitle()
    location = get_location()
    skills = get_keyskills()
    return render_template("form.html", title=title, locations=location, skills=skills)

def expfilter(x, exp):
    if type(x) == str and "yrs" in x and "-" in x:
        s = str(x).split("-")
        a = int(s[0])
        b = int(s[1][:s[1].index("y")])
        if exp in range(a, b):
            return True
        elif exp==0 and exp==a:
            return True
        return False
    if str(exp) in x:
        return True
    return False


def salfilter(x,sal):
    if type(x) == str and "-" in x and "pa." in x.lower():  # if cr crore lkh lakh la
        x = x[:x.index("pa")+2]
        s=str(x).split('-')
        p=s[0].replace(',','').strip()
        q=s[1].replace(',','').strip()
        try:
            a=int(p)
            b=int(q[:q.index("p")])
        except:
            return False
        else:
            if sal in range(a,b):
                return True
            else:
                return False
    return False

def filter_data(skills, exp, title, loc, sal):
    temp = pd.read_csv("../cleaned.csv", usecols=range(2, 14))
    if loc:
        temp = temp[temp['Location'].apply(lambda x:True if loc.lower() in str(x).lower() else False)]
    if skills:
        temp = temp[temp['Key Skills'].apply(lambda x:True if skills.lower() in str(x).lower() else False)]
    if len(exp)!=0:
        temp = temp[temp['Job Experience Required'].apply(lambda x:expfilter(str(x), int(exp)))]
    if sal:
        temp = temp[temp['Job Salary'].apply(lambda x: salfilter(str(x),int(sal)))]
    if title:
        temp = temp[temp['Job Title'].apply(lambda x:True if title.lower() in str(x).lower() else False)]
    return temp.to_html()

@app.route("/fetch_details/", methods=['GET', 'POST'])
def fetch_details():
    if request.method == "POST":
        name = request.form.get("fname")
        loc = request.form.get("location")
        skills = request.form.get("skills")
        exp = request.form.get("exp")
        title = request.form.get("title")
        city = request.form.get("city")
        sal = request.form.get("sal")
        return filter_data(skills, exp, title, loc, sal)
    return redirect(url_for("index")) 
app.run(host="localhost", debug=True)

