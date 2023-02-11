"""Имплементация сканера на базе протокола HTTP."""
from smart_greed import interfaces
from smart_greed.data_formats.moex.main import MoexFormat
from smart_greed.scanners.moex_using_requests import cfg


class HTTPScanner(interfaces.AbsScanner):
    """Имплементация сканера на базе протокола HTTP."""

    def parse_config(
            self,
            base_config: interfaces.BaseConfig,
    ) -> cfg.Config:
        """Выделить из большого конфига нужные нам элементы."""
        return cfg.Config(**base_config[self._type])

    def get_data(self) -> MoexFormat:
        """Получить данные из API."""
        # TODO - написать имплементацию
        print('Сканер работает')
        return MoexFormat()
