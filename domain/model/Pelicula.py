


class Pelicula:


    #Contructor de  la clase

    def __init__(self, id, titulo , anio, calificacion, duracion, descripcion , estado , director, categoria):
        self.__id = id  # _ => Protected  , __ => private
        self.__titulo = titulo
        self.__anio = anio
        self.__calificacion = calificacion
        self.__duracion = duracion
        self.__descripcion = descripcion
        self.__estado = estado
        self.__director = director
        self.__categoria = categoria




    #Getter and Setter


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        self.__anio = anio

    @property
    def calificacion(self):
        return self.__calificacion

    @calificacion.setter
    def calificacion(self, calificacion):
        self.__calificacion = calificacion

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        self.__director = director

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria


    ##  Metodos propios