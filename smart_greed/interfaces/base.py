"""Общие компоненты для интерфейсов.
"""
import abc
import contextlib
from typing import Iterator

from smart_greed import interfaces


class BaseExecutor(abc.ABC):
    """Базовый класс для сканера и презентера."""

    def __init__(
            self,
            base_config: interfaces.BaseConfig,
            my_type: str = '',
    ) -> None:
        """Инициализировать экземпляр."""
        self._type = my_type
        self.config = self.parse_config(base_config)

    def start_hook(self) -> None:
        """Произвольный код, который вызывается перед началом работы."""

    def stop_hook(self) -> None:
        """Произвольный код, который вызывается после окончания работы."""

    @contextlib.contextmanager
    def run(self) -> Iterator[None]:
        """Неявно вызывает start_hook и stop_hook."""
        self.start_hook()
        yield
        self.stop_hook()

    @abc.abstractmethod
    def parse_config(
            self,
            base_config: interfaces.BaseConfig,
    ) -> interfaces.AbsConfig:
        """Выделить из большого конфига нужные нам элементы."""
