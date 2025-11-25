from persistence.Conexion import Conexion


class UsuarioFreeRepositorio:

    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='movie_recommender_DB')
        self.db.connect()