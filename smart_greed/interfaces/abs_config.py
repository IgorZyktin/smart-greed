"""Абстрактный формат конфигурации."""
from collections import UserDict
from typing import Any

from pydantic import BaseModel


class BaseConfig(UserDict[str, Any]):
    """Абстрактная базовая конфигурация (фактически словарь)."""


class AbsConfig(BaseModel):
    """Абстрактная конфигурация.

    Будет своя у каждого компонента.
    """
