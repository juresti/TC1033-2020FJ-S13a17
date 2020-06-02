from claseApagador import Apagador
from claseFoco import Foco

class Lampara:
    def __init__(self,color = "Cafe",costo = 344):#composición
    #def __init__(self,color = "Cafe",costo = 344,apagador): #agregación
        self.__color = color
        self.__costo = costo
        self.__foco = Foco(100,"Azul") #composición
        self.__apagador = Apagador() #composición
        #self.__apagador = apagador #agregación
        
    @property
    def color(self):
        return self.__color
    
    @property
    def costo(self):
        return self.__costo
    @costo.setter
    def costo(self,costo):
        self.__costo = costo
        
    def encender(self):
        self.__apagador.encender()
        return "La lampara se encendio"
        
    def apagar(self):
        self.__apagador.apagar()
        return "La lampara se apagó"
    
    def isEncendida(self):
        return self.__apagador.isEncendido()
    
    def cambiarFoco(self,lum,color):
        self.__foco = Foco(lum,color)
        return f"Foco cambiado: {self.__foco}"
    
    def datosFoco(self):
        return self.__foco.luminosidad,self.__foco.color
    
    def __repr__(self):
        return f"Lampara({self.color},{self.costo},{repr(self.__foco)},{repr(self.__apagador)})"
    
    def __str__(self):
        strFoco = str(self.__foco)
        strApag = str(self.__apagador)
        strLamp = f"Lampara de color {self.color} que vale {self.costo}"
        return strLamp + ". Con un " + strFoco + ". " + strApag
    
if __name__ == "__main__":
    lamp1 = Lampara()
    lamp2 = Lampara("Morada",950)
    print(repr(lamp1))
    print(lamp2)
    print(lamp1.cambiarFoco(100,"Rojo"))
    print(lamp1)
    print(lamp2.encender())
    print(repr(lamp2))
    print(lamp2.datosFoco())
    print(lamp2.isEncendida())