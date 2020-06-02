class Foco:
    def __init__(self,luminosidad = 60,color = "Blanco"):
        self.__luminosidad = luminosidad
        self.__color = color
        
    @property
    def luminosidad(self):
        return self.__luminosidad
    
    @property
    def color(self):
        return self.__color
    
    def __repr__(self):
        return f"Foco({self.luminosidad},{self.color})"
    
    def __str__(self):
        return f"Foco color {self.color} de luminosidad {self.luminosidad}"
    
if __name__ == "__main__":
    miFoco = Foco()
    otro = Foco(100,"Verde")
    print(miFoco)
    print(repr(otro))
    print(miFoco.luminosidad)
    print(otro.color)
    