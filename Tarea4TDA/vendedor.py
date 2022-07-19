class Vendedor:
    def __init__(self, Id_vendedor=0, Nombre="", Contraseña_vendedor="", Venta_realizada=0) ->None:
        self.__id_vendedor=Id_vendedor
        self.__nombre=Nombre
        self.__contraseña_vendedor=Contraseña_vendedor
        self.__venta_realizada=Venta_realizada                

    @property
    def Id_vendedor(self)->int:
        return self.__id_vendedor
    @property
    def Nombre(self)->str:
        return self.__nombre   
    @property
    def Contraseña_vendedor(self)->str:
        return self.__contraseña_vendedor         
    @property
    def Venta_realizada(self)->int:
        return self.__venta_realizada        

    @Id_vendedor.setter
    def Id_vendedor(self, value)->None:
        self.__id_vendedor = value
    @Nombre.setter
    def Nombre(self, value)->None:
        self.__nombre = value
    @Contraseña_vendedor.setter
    def Contraseña_vendedor(self, value)->None:
        self.__contraseña_vendedor = value
    @Venta_realizada.setter
    def Venta_realizada(self, value)->None:
        self.__venta_realizada = value  