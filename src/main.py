from flask import Flask, request # library to create API
from src.checks.token_check import checkToken # Import function token validator

app = Flask('WannaEat') # API name


@app.route("/primaryRoute", methods=["GET"])
def primary_route(): # route function
    token = request.args.get('token')  # GET the token argument
    check = checkToken(token)   # token validator

    if False in check.keys():  # Check if token validator return False
        return check[False]

    dads = {check[True]:
                {'hello word': '123'}
            }  # Dads that will be returned

    return dads


app.run()
