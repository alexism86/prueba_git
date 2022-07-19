class Jefe_ventas:
    def __init__(self, Id_jefe=0, Nombre="", Contraseña_jefe="", Inventario_creado=0) ->None:
        self.__id_jefe=Id_jefe
        self.__nombre=Nombre
        self.__contraseña_jefe=Contraseña_jefe
        self.__inventario_creado=Inventario_creado                

    @property
    def Id_jefe(self)->int:
        return self.__id_jefe
    @property
    def Nombre(self)->int:
        return self.__nombre   
    @property
    def Contraseña_jefe(self)->str:
        return self.__contraseña_jefe         
    @property
    def Inventario_creado(self)->int:
        return self.__inventario_creado        

    @Id_jefe.setter
    def Id_jefe(self, value)->None:
        self.__id_jefe = value
    @Nombre.setter
    def Nombre(self, value)->None:
        self.__nombre = value
    @Contraseña_jefe.setter
    def Contraseña_jefe(self, value)->None:
        self.__contraseña_jefe = value
    @Inventario_creado.setter
    def Inventario_creado(self, value)->None:
        self.__inventario_creado = value  