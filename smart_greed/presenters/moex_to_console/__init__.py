"""Шаблонный код получения экземпляра."""
from smart_greed import interfaces

__all__ = [
    'get_instance',
]


def get_instance(
        base_config: interfaces.BaseConfig,
        scanner_type: str,
) -> interfaces.AbsPresenter:
    """Получить экземпляр клиента."""
    from smart_greed.presenters.moex_to_console import main
    return main.MoexToConsole(base_config, scanner_type)
