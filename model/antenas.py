from model.conexion_db import get_conexion_db
from loguru import logger
class Antenas():
    def get_antenas_activas(self):
        conn = get_conexion_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `antenas` WHERE estado='activo'")
        logger.info("Conexión a la DB cerrada correctamente")
        resul = cursor.fetchall()
        logger.success("Consulta ejecutada correctamente")
        conn.close()
        return resul
        


