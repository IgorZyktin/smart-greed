"""Шаблонный код получения экземпляра."""
from smart_greed import interfaces

__all__ = [
    'get_instance',
]


def get_instance(
        base_config: interfaces.BaseConfig,
        scanner_type: str,
) -> interfaces.AbsScanner:
    """Получить экземпляр клиента."""
    from smart_greed.scanners.moex_using_requests import main
    return main.HTTPScanner(base_config, scanner_type)
