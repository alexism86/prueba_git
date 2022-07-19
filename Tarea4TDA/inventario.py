class Inventario:
    def __init__(self, Id_inventario=0, Cantidad_prod=0) ->None:
        self.__id_inventario=Id_inventario
        self.__cantidad_prod=Cantidad_prod                        

    @property
    def Id_inventario(self)->int:
        return self.__id_inventario
    @property
    def Cantidad_prod(self)->int:
        return self.__cantidad_prod   
            

    @Id_inventario.setter
    def Id_inventario(self, value)->None:
        self.__id_inventario = value
    @Cantidad_prod.setter
    def Cantidad_prod(self, value)->None:
        self.__cantidad_prod = value 