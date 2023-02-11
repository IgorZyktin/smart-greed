"""Абстрактный сканер."""
import abc

from smart_greed import interfaces
from smart_greed.interfaces.base import BaseExecutor


class AbsScanner(BaseExecutor):
    """Абстрактный сканер.

    Выполняет получение данных от API.
    """

    @abc.abstractmethod
    def get_data(self) -> interfaces.AbsFormat:
        """Получить данные из API.

        Формат данных определяется имплементацией.
        """
