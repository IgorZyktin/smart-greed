"""Фикстуры общие для всего проекта."""
import os.path
import tempfile
from unittest import mock

import pytest

from tests import helpers


@pytest.fixture
def fake_base_config():
    """Вернуть фальшивый базовый конфиг."""
    with tempfile.TemporaryDirectory() as local_dir:
        filename = 'test.toml'
        path = os.path.join(local_dir, filename)
        with mock.patch('smart_greed.base_cfg.CONFIG_FILENAME', path):
            yield helpers.FakeBaseConfig(local_dir, filename)


@pytest.fixture
def fake_scanner():
    """Вернуть фальшивый сканер."""

    with mock.patch('smart_greed.scanners.importlib') as fake_importlib:
        def fake_getter(base_config, scanner_type):
            instance = helpers.FakeScanner(base_config, scanner_type)
            fake_importlib.instance = instance
            return instance

        fake_importlib.import_module.return_value = mock.Mock()
        fake_importlib.import_module.return_value.get_instance = fake_getter
        yield fake_importlib


@pytest.fixture
def fake_presenter():
    """Вернуть фальшивый презентер."""

    with mock.patch('smart_greed.presenters.importlib') as fake_importlib:
        def fake_getter(base_config, my_type):
            instance = helpers.FakePresenter(base_config, my_type)
            fake_importlib.instance = instance
            return instance

        fake_importlib.import_module.return_value = mock.Mock()
        fake_importlib.import_module.return_value.get_instance = fake_getter
        yield fake_importlib
