from .database import DataBaseClient
from .parser import ParserService
from .locale import I18N


class Client:
    def __init__(self) -> None:
        self.database: DataBaseClient = DataBaseClient()
        self.i18n: I18N = I18N()

    def parser(self):
        ...
