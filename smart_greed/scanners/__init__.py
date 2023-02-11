"""Пакет со сканерами. Под каждый источник данных свой.
"""
import importlib

from smart_greed import interfaces

__all__ = [
    'get_scanner',
]


def get_scanner(
        base_config: interfaces.BaseConfig,
) -> interfaces.AbsScanner:  # pragma: no cover
    """Вернуть экземпляр сканера."""
    scanner_type = base_config['user']['scanner_type']
    module = importlib.import_module(
        f'smart_greed.scanners.{scanner_type}'
    )
    return module.get_instance(base_config, scanner_type)  # noqa
