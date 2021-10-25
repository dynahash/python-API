from flask import Flask, request  # library to create API
from src.functions.functions import registerr #import function register



app = Flask('WannaEat')  # API name

@app.route("/register", methods=["GET"])
def register():  # route function
    if request.method == "GET":
        print(registerr())
        return str(registerr()).encode('utf-8', 'ignore').decode('utf-8')




app.run()
