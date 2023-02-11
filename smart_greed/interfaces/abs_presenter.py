"""Абстрактный презентер."""
import abc
from typing import Any

from smart_greed.interfaces.base import BaseExecutor


class AbsPresenter(BaseExecutor):
    """Абстрактный презентер.

    Выполняет форматирование и вывод данных в человеко-читаемом виде.
    """

    @abc.abstractmethod
    def present(self, data: Any) -> None:
        """Вывести данные в человеко-читаемом виде.

        Формат данных определяется имплементацией.
        Но должен быть наследником interfaces.AbsFormat.
        """
