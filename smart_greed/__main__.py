"""Стартовый пакет приложения.
"""
from smart_greed import base_cfg
from smart_greed import presenters
from smart_greed import scanners

DIRECTORY_FOR_SCANS = 'data'


def main():
    """Главный поток управления."""
    base_config = base_cfg.get_base_config()

    scanner = scanners.get_scanner(base_config)

    with scanner.run():
        data = scanner.get_data()

    data.save(data.serialize(), DIRECTORY_FOR_SCANS)

    presenter = presenters.get_presenter(base_config)

    with presenter.run():
        presenter.present(data)

    return data


if __name__ == '__main__':
    main()  # pragma: no cover
