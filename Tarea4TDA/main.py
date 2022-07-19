import imp
from os import cpu_count, system
from Conexion import Conexion
from Productos import Productos
from Producto_dao import ProductoDao
from Venta import venta
from venta_dao import VentaDao
from vendedor import Vendedor
from vendedor_dao import VendedorDao
from jefe_ventas import Jefe_ventas
from jefe_ventasdao import JefeVentasDao
from inventario import Inventario
from inventariodao import InventarioDao
from factura import Factura
from facturadao import FacturaDao
from boleta import Boleta
from boletadao import BoletaDao
from beautifultable import BeautifulTable
from time import sleep


Conexion.getStartConnection()

system( 'cls' )

dao_producto = ProductoDao()
dao_venta = VentaDao()
dao_vendedor = VendedorDao()
dao_jefeventas = JefeVentasDao()
dao_inventario = InventarioDao()
dao_factura = FacturaDao()
dao_boleta = BoletaDao()


menu = BeautifulTable()
menu.columns.header = ["   Incio de Sesion   "]
menu.rows.append(['1. Iniciar Sesion jefe de ventas'])
menu.rows.append(['2. Iniciar Sesion vendedor'])
menu.rows.append(['3. Ver Cuentas Jefe'])
menu.rows.append(['4. Ver Cuentas Vendedor'])
menu.rows.append(['5. Ver Inventario'])
menu.rows.append(['6. Ver Facturas Registradas'])
menu.rows.append(['7. Ver Boletas '])
menu.rows.append(['8. Cerrar Caja'])
menu.columns.alignment = BeautifulTable.ALIGN_LEFT

def IniciarSesionJefeVentas():
    system('cls')
    print('-------- Iniciar Sesion -------')
    
    Nombre = str(input('Ingresar usuario : ')).upper()
    Contraseña_jefe = str(input('Ingresar Contraseña : '))

    if dao_jefeventas.findByNombreJefeVentas(Nombre, Contraseña_jefe)==False:
        print(menu1)        
    else:
        print("Contraseña incorrecta")
    sleep(5)


    dao_jefeventas.JefeVentasList()

    dao_inventario.InventarioList()

    dao_factura.FacturaList()

    dao_boleta.BoletaList()


def IniciarSesionVendedor():
    system('cls')
    print('-------- Iniciar Sesion -------')
    
    Nombre = str(input('Ingresar usuario : ')).upper()
    Contraseña_vendedor = str(input('Ingresar Contraseña : '))

    if dao_vendedor.findByNombreVendedor(Nombre, Contraseña_vendedor)==False:
        print(menu1)
        
    else:
        print("Contraseña incorrecta")
    sleep(5)


    dao_vendedor.vendedorList()        
        
           
       


menu1 = BeautifulTable()
menu1.columns.header = ["   Bazar de la Nona   "]
menu1.rows.append(['1. Insertar Venta'])
menu1.rows.append(['2. Insertar Productos'])
menu1.rows.append(['3. Ver Venta'])
menu1.rows.append(['4. Ver Productos'])
menu1.rows.append(['5. Eliminar Producto'])
menu1.rows.append(['6. Actualizar Producto'])
menu1.rows.append(['7. Salir'])
menu1.columns.alignment = BeautifulTable.ALIGN_LEFT

def insertarVenta():
    system('cls')
    print('-------- NUEVA VENTA -------')
    Ingresar_venta = input('nombre: ').upper()
    if dao_venta.findByIngVenta(Ingresar_venta)==True:
        print("Nombre ya esta en la base de datos")
    else:
        Id_venta = int(input('Codigo de venta: '))
        Cantidad_venta = int(input('Cantidad:'))
        Generar_venta = str(input('Confirme venta: '))
        Detalle_producto= int(input('Producto: '))
        Informe_pdf= int(input('Negocio Factura: '))
        Detalle_boleta= int(input('Numero Boleta: '))
        Total= int(input('Total: '))

        dao_venta.ventaList()

        
        while True:
            Codigo = int(input('Codigo de producto: '))
            c = dao_producto.findByCodigo(Codigo)
            if c != None:
                break
            
        Venta = venta(Id_venta=Id_venta, Ingresar_Venta=Ingresar_venta, Cantidad_venta=Cantidad_venta, Generar_venta=Generar_venta, Detalle_producto=Detalle_producto, Informe_pdf=Informe_pdf, Detalle_boleta=Detalle_boleta, Total=Total)
        print( dao_venta.save(Venta) )
    sleep(5)

def insertarProducto():
    system('cls')
    print('-------- NUEVO PRODUCTO -------')
    Nombre = input('Nombre: ').upper()
    if dao_producto.findByNombre(Nombre)==True:
        print("Nombre ya esta en la base de datos")
    else:
        Codigo= int(input('Codigo $'))
        Nombre= str(input('Nombre: ') )       
        Cantidad= int(input('Cantidad $ '))
        Valor_unitario= int(input('Valor_unitario $ '))       


        dao_producto.productoList()

                
        while True:
            Codigo = int(input('codigo de producto: '))
            c = dao_producto.findByCodigo(Codigo)
            if c != None:
                break
            
        Productos = Productos(Nombre=Nombre, Cantidad=Cantidad, Valor_unitario=Valor_unitario)
        print( dao_producto.save(Productos) )
    sleep(5)

def eliminarProducto():
    system('cls')
    print('----------- Eliminar Producto ------------')
    dao_producto.productoList()
    codigo = int(input('codigo: '))
    print( dao_producto.delete(codigo) )
    sleep(5)

def actualizarProducto():
    system('cls')
    print('------------ Actualizar ------------')
    dao_producto.productoList()
    Codigo = int(input('Codigo: '))

    if dao_producto.findByCodigo(Codigo) != None:
        Valor_Unitario = int(input('Valor $'))
        Cantidad = int(input('Cantidad '))
        print( dao_producto.update(Valor_Unitario, Cantidad, Codigo) )
    else:
        print('codigo no existe')
    sleep(5)



while True:
    system('cls')
    print(menu)
    option = input("Opcion: ")
    if option == "1":
        IniciarSesionJefeVentas()        
    elif option == "2":
        system('cls')
        IniciarSesionVendedor()        
    elif option=="3":
        dao_jefeventas.JefeVentasList()
        sleep(5)
    elif option == "4":
        dao_vendedor.vendedorList()
        sleep(5)
    elif option == "5":
        dao_inventario.InventarioList()
        sleep(5)
    elif option == "6":
        dao_factura.FacturaList()
        sleep(5)
    elif option == "7":
        dao_boleta.BoletaList()
        sleep(5)
    elif option == "8":
        break
    else:
        print("option no valida")
        sleep(5)    

while True:
    system('cls')
    print(menu1)
    option = input("Opcion: ")
    if option == "1":
        insertarVenta()
    elif option == "2":
        insertarProducto()
        sleep(5)        
    elif option == "3":
        system('cls')
        dao_venta.ventaList()
        sleep(5)
    elif option=="4":
        dao_producto.productoList()
        sleep(5)
    elif option == "5":
        eliminarProducto()
        sleep(5)
    elif option == "6":
        actualizarProducto()
        sleep(5)
    elif option == "7":
        break
    else:
        print("option no valida")
        sleep(5)