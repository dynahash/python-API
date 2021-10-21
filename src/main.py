from flask import Flask, request  # library to create API
from src.functions.functions import registerr #import function register

app = Flask('WannaEat')  # API name

@app.route("/register", methods=["GET"])
def register():  # route function
    print(registerr())
    return registerr()



app.run()
