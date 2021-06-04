import pandas as pd
import numpy as np

data = pd.read_csv("../cleaned.csv", usecols=range(2, 14))

def get_keyskills():
    key_skills = []
    data['Key Skills'].apply(lambda x:key_skills.extend(str(x).lower().strip().split("|")) if type(x) == str else x)
    key_skills = pd.Series(list(map(lambda x: x.strip(), key_skills)))
    key_skills = key_skills[key_skills.apply(lambda x:True if len(x)<50 else False)]
    return key_skills

def get_location():
    location = []
    def change(x):
        l = " ".join(x.split(","))
        if "(" in l:
            i = l.index("(")
            l = l[:i]
        if "-" in l:
            i = l.index("-")
            l = l[:i]
        location.extend(l.split())
    data['Location'].apply(lambda x:change(x) if type(x) != float else np.nan)
    location = pd.Series(location).unique()
    return location

def get_jobtitle():
    jobtitle = data['Job Title'].unique()
    return jobtitle
