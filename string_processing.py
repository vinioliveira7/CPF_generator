from random import randint

def string_generator():
    cpf = str(randint(100000000, 999999999))

    return cpf


def complete_string_verification():
    cpf = string_generator()

    while cpf == cpf[0] * 9:
        cpf = string_generator()

    return cpf
