
from domain.model.Categoria import Categoria
from domain.service.Categoria_Service import Categoria_Service
from persistence.Categoria_Repositorio import Categoria_Repositorio


class TestCategoria:

    categoria = Categoria(None, None)
    categoria_service = Categoria_Service()

    categoria_service.crear_categoria()
    categoria_service.mostrar_categorias()