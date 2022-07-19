import cx_Oracle

class Conexion:
    connection=None
    cursor=None 

    @classmethod
    def getStartConnection(cls):
        cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_6")
        connect = cx_Oracle.connect(user="rodrigo", password="TallerSistemas2022", dsn="tallerdesarrollovespertino_high")
        cls.cursor = connect.cursor()
        cls.connection = connect


