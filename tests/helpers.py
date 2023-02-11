"""Вспомогательные компоненты для тестов."""
import os
from typing import Any
from unittest import mock

from smart_greed import interfaces


class FakeBaseConfig(interfaces.BaseConfig):
    """Фальшивый конфиг."""

    def __init__(self, directory: str, filename: str) -> None:
        """Инициализировать экземпляр."""
        super().__init__()
        self.directory = directory
        self.filename = filename
        self.mock = mock.Mock()

    def save(self, payload: str) -> None:
        """Сохранить предоставленный текст во временный файл."""
        path = os.path.join(self.directory, self.filename)
        with open(path, mode='w') as file:
            file.write(payload)


class FakeFormat(interfaces.AbsFormat):
    """Фальшивый формат данных."""

    def __init__(self, data: Any, filename: str = '') -> None:
        """Инициализировать экземпляр."""
        super().__init__(filename)
        self.data = data
        self.mock = mock.Mock()

    def serialize(self) -> dict[str, Any]:
        """Сериализовать данные в JSON-совместимый формат (не в строку)."""
        return dict(self.data)

    def save(
            self,
            serialized_data: dict[str, Any],
            directory: str,
    ) -> None:
        """Сохранить имеющиеся данные в виде JSON файла."""
        self.mock.save(serialized_data, directory)
        super().save(serialized_data, directory)


class FakeScannerConfig(interfaces.AbsConfig):
    """Фальшивый конфиг сканера."""
    x: int


class FakeScanner(interfaces.AbsScanner):
    """Фальшивый сканер."""

    def __init__(
            self,
            base_config: interfaces.BaseConfig,
            my_type: str = '',
    ) -> None:
        """Инициализировать экземпляр."""
        super().__init__(base_config, my_type)
        self.mock = mock.Mock()

    def parse_config(
            self,
            base_config: interfaces.BaseConfig,
    ) -> interfaces.AbsConfig:
        """Вернуть конфиг."""
        return FakeScannerConfig(**base_config['test_scanner'])

    def get_data(self) -> FakeFormat:
        """Вернуть тестовый формат данных."""
        data = FakeFormat({'test': True})
        self.mock.get_data.return_value = data
        self.mock.get_data()
        return data


class FakePresenterConfig(interfaces.AbsConfig):
    """Фальшивый конфиг презентера."""
    y: int


class FakePresenter(interfaces.AbsPresenter):
    """Фальшивый презентер."""

    def __init__(
            self,
            base_config: interfaces.BaseConfig,
            my_type: str = '',
    ) -> None:
        """Инициализировать экземпляр."""
        super().__init__(base_config, my_type)
        self.mock = mock.Mock()

    def parse_config(
            self,
            base_config: interfaces.BaseConfig,
    ) -> interfaces.AbsConfig:
        """Вернуть конфиг."""
        return FakePresenterConfig(**base_config['test_presenter'])

    def present(self, data: interfaces.AbsFormat) -> None:
        """Записать факт вызова"""
        self.mock.present(data)
