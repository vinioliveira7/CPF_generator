cpf = input("Digite um CPF [xxx.xxx.xxx-xx]: ")

def string_processor():

    digit_list = cpf[0:11].replace('.', '')
    treated_cpf = (digit_list)

    return treated_cpf

def complete_string_processor():

    digit_list = cpf.replace('.', '')
    digit_list = digit_list.replace('-', '')
    
    treated_cpf = digit_list

    if treated_cpf == treated_cpf[0] * 11:
        return False

    return treated_cpf