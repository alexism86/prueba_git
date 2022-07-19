
class Productos:
    def __init__(self, Codigo=0, Nombre="", Cantidad=0, Valor_unitario=0) ->None:
        self.__Codigo=Codigo
        self.__Nombre=Nombre
        self.__Cantidad=Cantidad
        self.__Valor_unitario=Valor_unitario        

    @property
    def Codigo(self)->int:
        return self.__Codigo
    @property
    def Nombre(self)->str:
        return self.__Nombre   
    @property
    def Cantidad(self)->int:
        return self.__Cantidad         
    @property
    def Valor_unitario(self)->int:
        return self.__Valor_unitario    

    @Codigo.setter
    def Codigo(self, value)->None:
        self.__Codigo = value
    @Nombre.setter
    def Nombre(self, value)->None:
        self.__Nombre = value
    @Cantidad.setter
    def Cantidad(self, value)->None:
        self.__Cantidad = value
    @Valor_unitario.setter
    def Valor_unitario(self, value)->None:
        self.__Valor_unitario = value    
        