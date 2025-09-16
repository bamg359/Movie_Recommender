
from domain.model.Categoria import Categoria
from domain.model.Pelicula import Pelicula
from domain.service.Pelicula_Service import PeliculaService


class Test_Pelicula:

    categoria = Categoria(None,None)
    pelicula = Pelicula(None,None,None,None,None,None,None,None,None)
    pelicula_service = PeliculaService()



    pelicula_service.crear_pelicula(pelicula,categoria)





