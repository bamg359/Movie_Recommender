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

    def mostrar_categoria_por_id(self):
        print("Categoria por ID")
        id_categoria = int(input("Ingrese el id de la Categoria a buscar"))
        categoria = self.categoria_repositorio.listar_categoria_por_id(id_categoria)
        print(f"Categoria {categoria}")


    def actualizar_categoria_por_id(self):
        id_categoria = int(input("Ingrese el id de la Categoria a actualizar"))
        nombre_cat = input("Ingrese el nombre de la categoria a actualizar")
        self.categoria.id_categoria = id_categoria
        self.categoria.categoria = nombre_cat
        self.categoria_repositorio.actualizar_categoria(id_categoria, self.categoria)

    def borrar_categoria(self):
        id_categoria = int(input("Ingrese el id de la categoria a borrar"))
        self.categoria_repositorio.eliminar_categoria(id_categoria)




