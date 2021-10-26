from flask import request  # library to create API
from src.checks.token_check import checkToken  # Import function token validator
from src.functions.password import password_filter
import psycopg2
from decouple import config




def registerr():  # route function

    database_user, database_password = config("DATABASE_USER"), config("DATABASE_PASSWORD")

    mydb = psycopg2.connect(
        database=database_user,
        user=database_user,
        password=database_password,
        host='motty.db.elephantsql.com',
        port='5432'
    )

    cursor = mydb.cursor()

    token = request.args.get('token')  # GET token argument
    user = request.args.get('user')  # GET user argument
    senha = request.args.get('senha')  # GET senha argument
    csenha = request.args.get('csenha')  # GET csenha argument
    email = request.args.get('email')  # GET email argument
    nmatricula = request.args.get('nmatricula')  # GET matricula argument
    lista = [token, user, senha, csenha, email, nmatricula]
    for i in lista:
        if len(i) > 20 and email != i:
            return ["False", "nenhum campo deve haver mais de 20 caracteres"]
    if '' in lista:
        return ["False", "Preencha todos os campos!"]
    check_token = checkToken(token)  # token validator
    check_password = password_filter(senha, csenha)
    # -------------------------------------------------------------------
    # Check if token validator return False
    if False in check_token.keys():
        return check_token[False]

    elif "False" in check_password:
        return check_password

    if "@" in email:
        pass
    else:
        return ["False", "Nenhum E-mail foi detectado."]
    # -------------------------------------------------------------------
    sqlinsert = f"SELECT user_name FROM register WHERE user_name = '{user}'"

    cursor.execute(sqlinsert)
    if cursor.fetchone() == None:
        pass
    else:
        return ["False", "Já existe alguém com esse nome de usuário"]

    sqlinsert = f"INSERT INTO register (user_name, user_password, user_email, matricula) VALUES (%s, %s, %s, %s)"
    dados = (user, senha, email, nmatricula)

    cursor.execute(sqlinsert, dados)
    mydb.commit()

    return ["True", "Conta criada com sucesso!"]