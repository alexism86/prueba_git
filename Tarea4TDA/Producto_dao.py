from Conexion import Conexion
from beautifultable import BeautifulTable

from Productos import Productos


class ProductoDao:

    def save(self, Productos)->str:
        if self.findByNombre(Productos.nombre)==False:
            Conexion.cursor.execute("insert into productos values(:0,:1,:2,:3)",[Productos.Codigo, Productos.Nombre, Productos.Cantidad, Productos.Valor_unitario])
            Conexion.connection.commit()
            return "Producto Creado"
        return "Nombre ya esta en la BD..."


    def findByNombre(self, Nombre) -> bool:
        Conexion.cursor.execute("select * from productos where nombre=:1",[Nombre])
        row = Conexion.cursor.fetchone()
        if row is None:
            return False
        return True


    def findByCodigo(self, Codigo) -> Productos:
        Conexion.cursor.execute("select * from productos where codigo=:0",[Codigo])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        return Productos(row[0],row[1],row[2],row[3])
    
    def delete(self, Codigo)->str:
        if self.findByCodigo(Codigo) != None:
            Conexion.cursor.execute("delete from productos where codigo=:1",[Codigo])
            Conexion.connection.commit()
            return "Producto eliminado"
        return "Codigo No encontrado..."
    
    def update(self, codigo, precio, stock)->str:
        if self.findByCodigo(codigo) != None:
            Conexion.cursor.execute("update productos set precio=:1, stock=:2 where codigo=:3", [precio, stock, codigo])
            Conexion.connection.commit()
            return "Producto Actualizado"


    def productoList(self)->None:
        tabla = BeautifulTable()
        tabla.columns.header=['CODIGO', 'NOMBRE', 'CANTIDAD', 'VALOR UNITARIO']
        for row in Conexion.cursor.execute('select * from PRODUCTOS order by codigo'):
            tabla.rows.append(row)

        print(tabla)
      


        
