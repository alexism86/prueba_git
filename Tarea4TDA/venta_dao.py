from Conexion import Conexion
from beautifultable import BeautifulTable

from Venta import venta


class VentaDao:


    def save(self, Venta)->str:
        if self.findByNombre(venta.Ingresar_venta)==False:
            Conexion.cursor.execute("insert into VENTA values(:1,:2,:3,:4,:5,:6,:7,:8)",[Venta.Id_venta, Venta.Ingresar_venta , Venta.Cantidad_venta, Venta.Generar_venta, Venta.Detalle_producto, Venta.Informe_pdf, Venta.Detalle_boleta, Venta.Total])
            Conexion.connection.commit()
            return "Venta Ingresada"
        return "Venta ya esta en la BD..."


    def findByIngVenta(self, Ingresar_venta) -> bool:
        Conexion.cursor.execute("select * from VENTA where Ingresar_venta=:2",[Ingresar_venta])
        row = Conexion.cursor.fetchone()
        if row is None:
            return False
        return True


    def findByCodigo(self, Id_venta) -> venta:
        Conexion.cursor.execute("select * from venta where codigo=:1",[Id_venta])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        return venta(row[0],row[1],row[2],row[3], row[4])
    
    def delete(self, Id_venta)->str:
        if self.findById(Id_venta) != None:
            Conexion.cursor.execute("delete from VENTA where codigo=:1",[Id_venta])
            Conexion.connection.commit()
            return "Producto eliminado"
        return "Codigo No encontrado..."
    
    def update(self, Id_venta, Cantidad_venta)->str:
        if self.findById(Id_venta) != None:
            Conexion.cursor.execute("update VENTA set Cantidad_venta=:1, where Id_venta=:3", [Cantidad_venta, Id_venta])
            Conexion.connection.commit()
            return "Producto Actualizado"


    def ventaList(self)->None:
        tabla = BeautifulTable()
        tabla.columns.header=['ID VENTA', 'INGRESAR VENTA', 'CANTIDAD VENTA', 'GENERAR VENTA', 'DETALLE PRODUCTO','INFORME PDF', 'DETALLE BOLETA', 'TOTAL']
        query="""SELECT v.id_venta, v.ingresar_venta, v.cantidad_venta, v.generar_venta, p.nombre, i.razon_social , b.id_boleta, v.total
                    FROM VENTA v
                    inner join PRODUCTOS p on v.detalle_producto = p.codigo
                    inner join FACTURA i on v.informe_pdf = i.id_factura
                    inner join BOLETA b on v.detalle_boleta = b.id_boleta
                    order by Id_venta
                """

        for item in Conexion.cursor.execute(query):
            tabla.rows.append(item)
        
        print(tabla)