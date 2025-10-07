from web.Menu_App import Menu_App


class App:


    def __init__(self):
        self.menu_app = Menu_App()



    def run_app(self):
        init = int(input("Ingrese 1 para inicializar la App "))

        while init != 0:

            opcion = int(input("1. Categoria 2. Peliculas 3. Salir"))

            match opcion:
                case 1:
                    print("Gestion de categoria")
                    init= True
                    self.menu_app.menu_categoria(init)
                case 2:
                    print("Gestion de peliculas")

                case 3:
                    print("Cerrando la Aplicación...")
                    init= 0



