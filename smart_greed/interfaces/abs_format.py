"""Абстрактный формат промежуточных данных."""
import abc
import datetime
import json
import os.path
from typing import Any


class AbsFormat(abc.ABC):
    """Абстрактный формат промежуточных данных.

    Результат работы сканера. Некая структура данных,
    которая хранит машино-читаемые результаты.
    """

    def __init__(self, filename: str = '') -> None:
        """Инициализировать экземпляр."""
        self.filename = filename or self.get_filename()

    def get_filename(self) -> str:
        """Получить имя для сохраняемого файла."""
        now = datetime.datetime.now()
        format_name = type(self).__name__
        filename = f'{now.isoformat()}_{format_name}.json'
        filename = filename.replace(':', '-').replace('T', '_')
        return filename

    def save(
            self,
            serialized_data: dict[str, Any],
            directory: str,
    ) -> None:
        """Сохранить имеющиеся данные в виде JSON файла."""
        payload = json.dumps(
            serialized_data,
            ensure_ascii=False,
        )

        path = os.path.join(directory, self.filename)
        with open(path, mode='w', encoding='utf-8') as file:
            json.dump(payload, file)

    @abc.abstractmethod
    def serialize(self) -> dict[str, Any]:
        """Сериализовать данные в JSON-совместимый формат (не в строку)."""
