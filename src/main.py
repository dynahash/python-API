from flask import Flask, request, jsonify
from flask.wrappers import Response
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, MethodNotAllowed

from utils import check_token, check_password

from re import search
from typing import Union, Dict, Any

app = Flask('WannaEat')  # API name
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.errorhandler(BadRequest)
def bad_request_error(error) -> Response:
    return jsonify({
        "message": str(error)
    })

@app.errorhandler(MethodNotAllowed)
def method_not_allowed_error(error) -> Response:
    return jsonify({
        "message": str(error)
    })

@app.route("/validate", methods=["GET"])
def validate() -> Union[Response, Exception]:
    """
    This will validate a login request
    """
    if request.method == "GET":
        allowed_args = ["token", "user", "password",
                        "correct_password", "email", "registry"]
        data = request.json

        IS_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

        for arg in allowed_args:
            if data.get(arg) is None or str(data[arg]).strip() == "":
                raise BadRequest(f"You have to provide a{'n' if arg == 'email' or arg == 'user' else ''} valid {arg}!")

        is_token_correct = check_token(data["token"])
        is_password_correct = check_password(
            data["password"], data["correct_password"])

        if is_token_correct == False or is_password_correct == False:
            raise BadRequest("Token or password are incorrect")

        if not search(IS_EMAIL, data["email"]):
            raise BadRequest("Impromer email has been provided")

        return jsonify({
            "message": "Account validated successfully!"
        })
    else:
        raise MethodNotAllowed(f"Method '{request.method}' is not allowed")


app.run()
