import re

def password_filter(password, cpassword):
    if password != cpassword:
        return["False", "A senha digitada não corresponde com a senha do campo `Digite a senha novamente` "]
    elif len(password) < 8:
        return ["False", "Coloque uma senha com mais de 8 caracteres!"]

    elif not re.search("[a-z]", password):
        return ["False", "Coloque alguma letra na senha!"]

    elif not re.search("[A-Z]", password):
        return ["False", "Coloque alguma letra maiúscula na senha"]

    else:
        return ["True", "Senha válida!"]


