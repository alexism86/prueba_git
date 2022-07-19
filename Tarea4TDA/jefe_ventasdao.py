from Conexion import Conexion
from beautifultable import BeautifulTable
from inventario import Inventario
from jefe_ventas import Jefe_ventas

class JefeVentasDao:
    
    def findByNombreJefeVentas(self, nombre, contraseña_jefe):
        for row in Conexion.cursor.execute("select * from Jefe_ventas"):
            if row [1] == nombre:
                if row [2] == contraseña_jefe:
                    return True
        return False

    def findById(self, contraseña_jefe)->Jefe_ventas:
        Conexion.cursor.execute("select * from Jefe_ventas where contraseña_jefe=:2", [contraseña_jefe])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        return Jefe_ventas(row[0],row[1],row[2],row[3])
   
    def JefeVentasList(self) -> None:
        tabla = BeautifulTable()
        tabla.columns.header=['ID', 'NOMBRE JEFE','CONTRASEÑA','CANTIDAD INVENTARIO']
        query="""SELECT j.id_jefe, j.nombre, j."CONTRASEÑA_JEFE", n.cantidad_prod
                    FROM jefe_ventas j
                    INNER JOIN INVENTARIO n on j.inventario_creado = n.id_inventario;"""
        for row in Conexion.cursor.execute('select * from Jefe_ventas order by id_jefe'):
            tabla.rows.append(row)
        print(tabla)