from conexion_db import conn
class Antenas():
    def __init__(self):
        self.cursor = conn.cursor()

    def get_antenas_activas(self):
        self.cursor.execute("SELECT * FROM `antenas` WHERE estado='activo'")
        return self.cursor.fetchall()


antena = Antenas()
antenas_activas = antena.get_antenas_activas()

for row in antenas_activas:
    print(row)