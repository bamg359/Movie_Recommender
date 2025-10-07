
from domain.model.Categoria import Categoria
from domain.service.Categoria_Service import Categoria_Service
from persistence.Categoria_Repositorio import Categoria_Repositorio
from web.App import App


class TestCategoria:

    app = App()

    app.run_app()