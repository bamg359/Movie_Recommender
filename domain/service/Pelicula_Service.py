

class PeliculaService:


    def __init__(self, pelicula):
        self.pelicula = pelicula



    def crear_pelicula(self, pelicula):
        id = int(input("Ingrese el ID de la pelicula: "))
        self.pelicula.id = id
        titulo = input("Ingrese el nombre de la pelicula: ")
        self.pelicula.titulo = titulo
        anio = input("Ingrese el año de estreno de la pelicula: ")
        self.pelicula.anio = anio
        calificacion = input("Ingrese el calificacion de la pelicula: ")
        self.pelicula.calificacion = calificacion
        duracion = input("Ingrese la duracion de la pelicula: ")
        self.pelicula.duracion = duracion
        estado = input("Ingrese la estado de la pelicula: ")
        self.pelicula.estado = estado
        categoria = input("Selecciones la categoria de la pelicula: ")
        self.pelicula.categoria = categoria
        director = input("Ingrese el director de la pelicula: ")
        self.pelicula.director = director

    def listar_peliculas(self):
        return self.pelicula

    def buscar_id(self, id):
        return self.pelicula.id

    def actualizar_pelicula(self, pelicula):
        id = int(input("Ingrese el ID de la pelicula: "))


    def eliminar_pelicula(self, id):
        id = int(input("Ingrese el ID de la pelicula: "))






