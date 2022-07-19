from Conexion import Conexion
from beautifultable import BeautifulTable

from vendedor import Vendedor

class VendedorDao:
    
    def findByNombreVendedor(self, nombre, contraseña_vendedor):
        for row in Conexion.cursor.execute("select * from vendedor"):
            if row [1] == nombre:
                if row [2] == contraseña_vendedor:
                    return True
        return False

    def findById(self, contraseña_vendedor)->Vendedor:
        Conexion.cursor.execute("select * from vendedor where contraseña_vendedor=:2", [contraseña_vendedor])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        return Vendedor(row[0],row[1],row[2],row[3])
   
    def vendedorList(self) -> None:
        tabla = BeautifulTable()
        tabla.columns.header=['ID', 'NOMBRE','CONTRASEÑA','VENTAS']
        for row in Conexion.cursor.execute('select * from VENDEDOR order by id_vendedor'):
            tabla.rows.append(row)

        print(tabla)