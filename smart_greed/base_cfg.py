"""Инструменты для работы с базовой конфигурацией.
"""
import tomli

from smart_greed import interfaces

CONFIG_FILENAME = 'config.toml'


def get_base_config() -> interfaces.BaseConfig:
    """Получить общий конфиг для всего приложения.

    Каждый компонент возьмёт из него те данные, что ему нужны.

    Пример результата:
    {
        'user': {
            'scanner_type': 'moex_using_requests',
            'presenter_type': 'moex_to_console'
        },
        'moex_using_requests': {},
        'moex_to_console': {}
    }
    """
    with open(CONFIG_FILENAME, mode='rb') as fp:
        config = tomli.load(fp)

    return interfaces.BaseConfig(config)
