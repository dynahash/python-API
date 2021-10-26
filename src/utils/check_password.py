from typing import Union

from werkzeug.exceptions import BadRequest

def check_password(password: str, cpassword: str) -> Union[bool, Exception]:
    return password == cpassword
    # the oher conditional expressions are unusual,
    # if you consider that most part of them
    # would only be useful when the user
    # is creating an account,
    # not validating an existing one