class Boleta:
    def __init__(self, Id_boleta=0, Detalle_prod=0, Cantidad_p="", Total=0) ->None:
        self.__id_boleta=Id_boleta
        self.__detalle_prod=Detalle_prod
        self.__cantidad_p=Cantidad_p
        self.__total=Total                

    @property
    def Id_boleta(self)->int:
        return self.__id_boleta
    @property
    def Detalle_prod(self)->int:
        return self.__detalle_prod   
    @property
    def Cantidad_p(self)->str:
        return self.__cantidad_p         
    @property
    def Total(self)->int:
        return self.__total        

    @Id_boleta.setter
    def Id_boleta(self, value)->None:
        self.__id_boleta = value
    @Detalle_prod.setter
    def Detalle_prod(self, value)->None:
        self.__detalle_prod = value
    @Cantidad_p.setter
    def Cantidad_p(self, value)->None:
        self.__cantidad_p = value
    @Total.setter
    def Total(self, value)->None:
        self.__total = value      
        