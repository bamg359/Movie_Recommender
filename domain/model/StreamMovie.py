from domain.model.Pelicula import Pelicula
from domain.model.Usuario_Free import Usuario_free


class StreamMovie:


    def __init__(self, id_play, play_date, movie, usuario):
        self.id_play= id_play
        self.play_date = play_date
        self.movie = Pelicula(None,None,None,None,None,None,
                              None,None,None)
        self.usuario = Usuario_free(None,None,None,None,None,None)
