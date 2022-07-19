class Factura:
    def __init__(self, Id_factura=0, Razon_Social="", Rut_cliente="", Giro="", Direccion="",Detalle_p=0) ->None:
        self.__id_factura=Id_factura
        self.__razon_social=Razon_Social
        self.__rut_cliente=Rut_cliente
        self.__giro=Giro
        self.__direccion=Direccion
        self.__detalle_p=Detalle_p        

    @property
    def Id_factura(self)->int:
        return self.__id_factura
    @property
    def Razon_Social(self)->str:
        return self.__razon_social   
    @property
    def Rut_cliente(self)->int:
        return self.__rut_cliente         
    @property
    def Giro(self)->int:
        return self.__giro
    @property
    def Direccion(self)->int:
        return self.__direccion
    @property
    def Detalle_p(self)->int:
        return self.__detalle_p    

    @Id_factura.setter
    def Id_factura(self, value)->None:
        self.__id_factura = value
    @Razon_Social.setter
    def Razon_Social(self, value)->None:
        self.__razon_social = value
    @Rut_cliente.setter
    def Rut_cliente(self, value)->None:
        self.__rut_cliente = value
    @Giro.setter
    def Giro(self, value)->None:
        self.__giro = value
    @Direccion.setter
    def Direccion(self, value)->None:
        self.__direccion = value
    @Detalle_p.setter
    def Detalle_p(self, value)->None:
        self.__detalle_p = value    
        