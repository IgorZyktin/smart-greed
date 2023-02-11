"""Пакет со презентерами. Под каждый источник данных свой.
"""
import importlib

from smart_greed import interfaces

__all__ = [
    'get_presenter',
]


def get_presenter(
        base_config: interfaces.BaseConfig,
) -> interfaces.AbsPresenter:
    """Вернуть экземпляр презентера."""
    presenter_type = base_config['user']['presenter_type']
    module = importlib.import_module(
        f'smart_greed.presenters.{presenter_type}'
    )
    return module.get_instance(base_config, presenter_type)  # noqa
