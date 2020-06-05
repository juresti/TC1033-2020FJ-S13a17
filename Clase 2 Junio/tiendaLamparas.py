from claseLampara import Lampara

def altaInventario(inventario):
    color = input("Dime el color de la lampara: ")
    costo = int(input("Dime el costo de la lampara: "))
    miLamp = Lampara(color,costo)
    inventario.append(miLamp)
    return inventario

def verPrimerLamp(inventario):
    lamp = inventario[0]
    lum,color = lamp.datosFoco()
    print(f"El foco es de color {color} de {lum} watts")