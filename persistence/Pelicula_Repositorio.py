
from persistence.Conexion import Conexion


class Pelicula_Repositorio:


    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='movie_recommender_DB')
        self.db.connect()




    def crear_pelicula_DB(self):
        query = "INSERT INTO  "




