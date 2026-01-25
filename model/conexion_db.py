import mysql.connector
from mysql.connector import errorcode
from loguru import logger
def get_conexion_db():
    try:
        #Se deben actualizar valores en base a la Base de datos
        conn = mysql.connector.connect(user='name', password='',
                              host='host',
                              database='db_name')
        logger.success("Conexión a la db correctamente")
        return conn
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error("Error en el usuario o contraseña en la BD")
            print("Error en el usuario o contraseña en la BD")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error("La DB no existe")
            print("La DB no existe")
        else:
            logger.error(err)
            print(err)

