"""Проверка базового функционала."""
from pathlib import Path
from unittest import mock

from smart_greed.__main__ import main

BASE_CONFIG = '''
[user]
scanner_type = "test_scanner"
presenter_type = "test_presenter"

[test_scanner]
x = 1

[test_presenter]
y = 2
'''


def test_basic(
        fake_base_config,
        fake_scanner,
        fake_presenter,
):
    """Убедиться, что главная механика вызова работает."""
    # Настройка
    fake_base_config.save(BASE_CONFIG)

    # Исполнение
    with mock.patch('smart_greed.__main__.DIRECTORY_FOR_SCANS',
                    fake_base_config.directory):
        data = main()

    # Проверка
    assert Path.exists(Path(fake_base_config.directory) / data.filename)

    assert fake_scanner.instance.config.x == 1
    fake_scanner.instance.mock.get_data.assert_has_calls([
        mock.call(),
    ])

    assert fake_presenter.instance.config.y == 2
    fake_presenter.instance.mock.present.assert_has_calls([
        mock.call(mock.ANY),
    ])
