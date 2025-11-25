from domain.model.Categoria import Categoria
from domain.service.Categoria_Service import Categoria_Service


class Menu_App():


    def __init__(self):
        self.categoria = Categoria(None, None)
        self.categoria_service = Categoria_Service()




    def menu_categoria(self, init):

        while init:
            opc = int(input("1. Crear categoria 2. Listar Categoria 3. Listar categoria por ID 4. Actualizar Categoria 5. Eliminar Categoria 6. Exportar CSV 7. Regresar Menu App "))

            match opc:
                case 1:
                    print("Crear Categoria")
                    self.categoria_service.crear_categoria()
                case 2:
                    print("Listado de Categorias")
                    self.categoria_service.mostrar_categorias()
                case 3:
                    print("Categorias por Id ")
                    self.categoria_service.mostrar_categoria_por_id()
                case 4:
                    print("Actualizar Categoria por ID")
                    self.categoria_service.actualizar_categoria_por_id()
                case 5:
                    print("Eliminar Categoria")
                    self.categoria_service.borrar_categoria()
                case 6:
                    print("Exportar CSV categoria")
                    self.categoria_service.exportar_csv_categoria()
                case 7:
                    print("Regresando al menú principal")
                    init  = False

