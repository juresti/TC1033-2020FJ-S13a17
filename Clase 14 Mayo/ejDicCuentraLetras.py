def cuentaLetras(palabra):
    dicc = {}
    palabra = palabra.lower()
    for letra in palabra:
        if letra in dicc:
            dicc[letra] += 1
        else:
            dicc[letra] = 1
    return dicc

