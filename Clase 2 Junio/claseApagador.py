class Apagador:
    def __init__(self):
        self.__encendido = False
        
    def encender(self):
        self.__encendido = True
        
    def apagar(self):
        self.__encendido = False
        
    def isEncendido(self): #get de encendido
        return self.__encendido
    
    def __repr__(self):
        return f"Apagador({self.__encendido})"
    
    def __str__(self):
        return f"El apagador se encuentra en {self.__encendido}"
    
if __name__ == "__main__":
    miApag = Apagador()
    print(miApag)
    miApag.encender()
    print(repr(miApag))
    print(miApag.isEncendido())
    