import re
from validate_docbr import CPF

def validate_cpf(value):
    cpf = CPF()
    return not cpf.validate(value)

def validate_nome(value):
    return not value.isalpha()

def validate_numero_telefone(value):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}' 
    resposta = re.findall(modelo, value)
    return not resposta