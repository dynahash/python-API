from flask import Flask, request  # library to create API
from flask_cors import CORS
from src.functions.functions import registerr #import function register

app = Flask('WannaEat')  # API name
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/register", methods=["GET"])
def register():  # route function
    return str(registerr()).encode('utf-8', 'ignore').decode('utf-8')

app.run()
