"""Imprime el valor de __name__ y lo verifica """

print(__name__)

if (__name__ == "__main__"):
    print("¡Que si soy main!")
else:
    print("Soy el modulo: " + __name__)