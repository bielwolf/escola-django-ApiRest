def validate_cpf(value):
    return len(value) != 11

def validate_nome(value):
    return not value.isalpha()

def validate_numero_telefone(value):
    return len(value) != 13
 