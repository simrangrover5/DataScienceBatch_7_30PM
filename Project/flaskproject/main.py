from flask import Flask

# app = Flask(__name__) 

# @app.route("/")  # @ --> route --> decorator
# def index():  
#    pass  


def deco(*args):
    print(args)
    def deco1(func):
        def func1(*mul):
            result = func(*mul)
            print(result)
        return func1 
    return deco1

#@deco("hello")
def add(a, b):
    return a+b

#add(10, 20)
d = deco("hello")
f = d(add)
f(10, 20)