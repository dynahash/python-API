from dotenv import load_dotenv
from os import getenv

# loading .env file
load_dotenv(dotenv_path=".env")

def check_token(token: str) -> bool:
    """
    This function will validate the
    provided token and return a
    boolean based on the validation.
    """
    return getenv("TOKEN_ADMIN") == token
