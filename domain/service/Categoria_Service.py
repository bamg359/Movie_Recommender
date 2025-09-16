from domain.model.Categoria import Categoria
from persistence.Categoria_Repositorio import Categoria_Repositorio


class Categoria_Service:

    def __init__(self):
        self.categoria = Categoria(None,None)
        self.categoria_repositorio = Categoria_Repositorio()


    def crear_categoria(self):
        nombre_categoria = input("Ingrese el nombre de la categoria: ")
        self.categoria.categoria = nombre_categoria
        self.categoria_repositorio.crear_categoria_DB(self.categoria)


    def mostrar_categorias(self):
        print("Lista de Categorias")
        lista_categorias = self.categoria_repositorio.listar_Categorias()
        print(f"Lista de categorias {lista_categorias}")


