from string_processing import complete_string_processor
from digit_verification import new_cpf


if complete_string_processor == False:
    print("CPF INVÁLIDO")
else:
    print("CPF VÁLIDO" if complete_string_processor() == new_cpf() else "CPF INVÁLIDO")

    

