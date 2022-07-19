from Conexion import Conexion
from beautifultable import BeautifulTable
from factura import Factura

class FacturaDao:
    def save(self, Factura)->str:
        if self.findByFactura(Factura.razon_social)==False:
            Conexion.cursor.execute("insert into factura values(:0,:1,:2,:3,:4,:5)",[Factura.id_factura, Factura.razon_social, Factura.rut_cliente, Factura.giro, Factura.direccion, Factura.detalle_p])
            Conexion.connection.commit()
            return "Producto Creado"
        return "Nombre ya esta en la BD..."


    def findByFactura(self, id_factura):
        for row in Conexion.cursor.execute("select * from Factura"):
            if row [1] == id_factura:
                return True
        return False

    def findByIdFac(self, id_factura)->Factura:
        Conexion.cursor.execute("select * from Factura where id_factura=:0", [id_factura])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        return Factura(row[0],row[1],row[2],row[3],row[4],row[5])
    
   
    def FacturaList(self) -> None:
        tabla = BeautifulTable()
        tabla.columns.header=['ID', 'RAZON SOCIAL', 'RUT CLIENTE', 'GIRO', 'DIRECCION','CANTIDAD COMPRADA','CODIGO PRODUCTO', 'TOTAL']
        query="""SELECT f.id_factura, f.razon_social, f.rut_cliente, f.giro, f.direccion, v.cantidad_venta, v.detalle_producto, v.total 
                    FROM factura f
                    INNER JOIN VENTA v on f.detalle_p = v.id_venta
                    ORDER BY id_factura"""
        for item in Conexion.cursor.execute(query):
            tabla.rows.append(item)
        print(tabla)