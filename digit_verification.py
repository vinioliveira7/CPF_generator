from string_processing import *

def digit1_verificator():

    treated_cpf = string_processor()
    cont = 10
    total = 0
    for digit in treated_cpf:
        digit = int(digit)
        value = digit * cont
        total += value
        cont -= 1
    result = 11 - (total % 11)
    return '0' if result > 9 else str(result)

def digit2_verificator():
    
    treated_cpf = string_processor() + digit1_verificator()
    cont = 11
    total = 0
    for digit in treated_cpf:
        digit = int(digit)
        value = digit * cont
        total += value
        cont -= 1
    result = 11 - (total % 11)
    return '0' if result > 9 else str(result)

def new_cpf():
    treated_cpf = string_processor() + digit1_verificator() +digit2_verificator()
    return treated_cpf
    






