"""Формат данных Московской биржи."""
from typing import Any

from smart_greed import interfaces


class MoexFormat(interfaces.AbsFormat):
    """Формат данных Московской биржи."""

    def serialize(self) -> dict[str, Any]:
        """Сериализовать данные в JSON-совместимый формат (не в строку)."""
        # TODO - написать имплементацию
        print('Данные сериализуются')
        return {}
