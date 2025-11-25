
from persistence.Conexion import Conexion
from domain.model.Categoria import Categoria
from datetime import datetime
import csv

class Categoria_Repositorio:

    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='movie_recommender_DB')
        self.db.connect()


    def crear_categoria_DB(self, categoria):
        query = "INSERT INTO categoria (nombre_categoria) VALUES (%s)"
        values = (categoria.categoria,)
        self.db.execute_query(query, values)


    def listar_Categorias(self):
        query = "SELECT * FROM categoria"
        result = self.db.execute_query(query)
        if result:
            categoria_lista = []
            for row in result:
                categoria  = Categoria.from_row(row)
                categoria_lista.append(categoria)
            return categoria_lista
        else:
            print("No se ha podido recuperar categorias")
            return []


    def listar_categoria_por_id(self, categoria_id):
        query = "Select * from categoria where id_categoria = %s"
        result = self.db.execute_query(query, (categoria_id,))
        if result:
            return Categoria.from_row(result[0])
        else:
            print("registro no encontrado")
            return []

    def actualizar_categoria(self, categoria_id, categoria):
        query = "UPDATE categoria set nombre_categoria = %s where id_categoria = %s "
        values = (categoria.categoria,categoria_id)
        self.db.execute_query(query, values)

    def eliminar_categoria(self, categoria_id):
        query = "DELETE FROM categoria where id_categoria = %s"
        self.db.execute_query(query, (categoria_id,))


    def exportar_csv_categoria(self,file_path = None):
        query = "SELECT * FROM categoria"
        result = self.db.execute_query(query)
        if not file_path:
            file_path = f"categoria_{datetime.now().strftime('%d-%m-%Y')}.csv"

            column_names = [desc[0] for desc in self.db.execute_query(query)]

            with open(file_path, mode='w', newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(column_names)
                writer.writerows(result)

            print(f"Archivo exportado correctamente{file_path} ")
            return file_path

        else:
            print("registros no encontrados")
            return []





