"""Имплементация презентера с выводом в консоль.
"""
from smart_greed import interfaces
from smart_greed.data_formats.moex.main import MoexFormat
from smart_greed.presenters.moex_to_console import cfg


class MoexToConsole(interfaces.AbsPresenter):
    """Имплементация презентера MOEX с выводом в консоль."""

    def parse_config(
            self,
            base_config: interfaces.BaseConfig,
    ) -> cfg.Config:
        """Выделить из большого конфига нужные нам элементы."""
        return cfg.Config(**base_config[self._type])

    def present(self, data: MoexFormat) -> None:
        """Вывести данные в человеко-читаемом виде."""
        # TODO - написать имплементацию
        print('Презентер работает')
