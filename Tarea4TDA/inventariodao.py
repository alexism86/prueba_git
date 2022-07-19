from Conexion import Conexion
from beautifultable import BeautifulTable
from inventario import Inventario
from jefe_ventas import Jefe_ventas

class InventarioDao:
    
    def findByNombreInventario(self, id_inventario, cantidad_prod):
        for row in Conexion.cursor.execute("select * from Inventario"):
            if row [1] == id_inventario:
                if row [2] == cantidad_prod:
                    return True
        return False

    def findByIdInv(self, id_inventario)->Inventario:
        Conexion.cursor.execute("select * from Inventario where id_inventario=:0", [id_inventario])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        return Inventario(row[0],row[1])

    def delete(self, id_inventario)->str:
        if self.findByIdInv(id_inventario) != None:
            Conexion.cursor.execute("delete from inventario where id_inventario=:0",[id_inventario])
            Conexion.connection.commit()
            return "Producto eliminado"
        return "Codigo No encontrado..."
   
    def InventarioList(self) -> None:
        tabla = BeautifulTable()
        tabla.columns.header=['CODIGO INVENTARIO', 'NOMBRE PRODUCTO','CANTIDAD PRODUCTO']
        query="""SELECT n.id_inventario, p.nombre, p.cantidad
                    FROM inventario n
                    inner join productos p on n.cantidad_prod = p.codigo
                    order by id_inventario"""
        for item in Conexion.cursor.execute(query):
            tabla.rows.append(item)
        print(tabla)