class venta:
    def __init__(self, Id_venta=0, Ingresar_Venta="", Cantidad_venta=0, Generar_venta="", Detalle_producto=0, Informe_pdf=0, Detalle_boleta=0, Total=0) ->None:
        self.__id_venta=Id_venta
        self.__ingresar_venta=Ingresar_Venta
        self.__cantidad_venta=Cantidad_venta
        self.__generar_venta=Generar_venta
        self.__detalle_producto=Detalle_producto
        self.__informe_pdf=Informe_pdf
        self.__detalle_boleta=Detalle_boleta
        self.__total=Total

    @property
    def Id_venta(self)->int:
        return self.__id_venta
    @property
    def Ingresar_venta(self)->str:
        return self.__ingresar_venta   
    @property
    def Cantidad_venta(self)->int:
        return self.__cantidad_venta         
    @property
    def Generar_venta(self)->str:
        return self.__generar_venta   
    @property
    def Detalle_producto(self)->int:
        return self.__detalle_producto
    @property
    def Informe_pdf(self)->int:
        return self.__informe_pdf
    @property
    def Detalle_boleta(self)->int:
        return self.__detalle_boleta
    @property
    def Total(self)->int:
        return self.__total  

    @Id_venta.setter
    def Id_venta(self, value)->None:
        self.__id_venta = value
    @Ingresar_venta.setter
    def Ingresar_venta(self, value)->None:
        self.__ingresar_venta = value
    @Cantidad_venta.setter
    def Cantidad_venta(self, value)->None:
        self.__cantidad_venta = value
    @Generar_venta.setter
    def Generar_venta(self, value)->None:
        self.__generar_venta = value
    @Detalle_producto.setter
    def Detalle_producto(self, value)->None:
        self.__detalle_producto = value
    @Informe_pdf.setter
    def Informe_pdf(self, value)->None:
        self.__informe_pdf = value
    @Detalle_boleta.setter
    def Detalle_boleta(self, value)->None:
        self.__detalle_boleta = value
    @Total.setter
    def Total(self, value)->None:
        self.__total = value