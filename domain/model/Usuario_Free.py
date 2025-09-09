from domain.model.Usuario import Usuario


class Usuario_free(Usuario):

    def __init__(self, id, nombre, correo, contrasena , flag_free , ads):
        super().__init__(id, nombre, correo, contrasena)
        self.__flag_free = flag_free
        self.__ads = ads


    ## Getter and Setter

