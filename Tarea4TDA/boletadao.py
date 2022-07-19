from Conexion import Conexion
from beautifultable import BeautifulTable
from boleta import Boleta

class BoletaDao:
    def findByIdBol(self, id_boleta)->Boleta:
        Conexion.cursor.execute("select * from Boleta where id_boleta=:0", [id_boleta])
        row = Conexion.cursor.fetchone()
        if row is None:
            return None
        return Boleta(row[0],row[1],row[0],row[1])    
   
    def BoletaList(self) -> None:
        tabla = BeautifulTable()
        tabla.columns.header=['NUMERO BOLETA', 'CANTIDAD','TOTAL']
        query="""SELECT  b.id_boleta, v.cantidad_venta, v.total
                    FROM BOLETA b
                    INNER JOIN VENTA v on b.detalle_prod = v.id_venta
                    ORDER BY id_boleta"""
        for item in Conexion.cursor.execute(query):
            tabla.rows.append(item)
        print(tabla)