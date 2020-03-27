from routes import api
from fastapi import FastAPI


def create_app() -> FastAPI:
    """
    Create The Application
    The first thing we will do is create a new application instance
    which serves as the "glue" for all the components of the api.
    :return: FastAPI
    """

    app = FastAPI(title='covid-19 Chile')
    app.include_router(api.router)

    return app


__version__ = '0.1.0'
