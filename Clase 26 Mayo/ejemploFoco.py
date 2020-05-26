class Foco:
    def __init__(self,encendido = False,costo = 1):
        self.__encendido = encendido
        self.__costo = costo
        
    def comparaFoco(self,otroFoco):
        "otroFoco es un objeto de tipo Foco"
        if(self.__costo < otroFoco.getCosto()):
            print(f"Mi precio es más barato, valgo {self.__costo}, el otro vale {otroFoco.getCosto()}")
        else:
            print(f"El otro foco es más barato, vale {otroFoco.getCosto()} y yo {self.__costo}")
        
    
    def getCosto(self):
        return self.__costo
    
    def setCosto(self,nCosto):
        if (nCosto >= 1) and (nCosto <= 10):
            self.__costo = nCosto
        else:
            print("Error en el costo")
            
if __name__ == "__main__":
    miFoco = Foco()
    print(miFoco.getCosto())
    miFoco.setCosto(44)
    miFoco.setCosto(4)
    print(miFoco.getCosto())
    foco2 = Foco(False,3)
    foco2.comparaFoco(miFoco)
    miFoco.comparaFoco(foco2)
    