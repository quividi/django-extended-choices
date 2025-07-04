"""Little helper application to improve django choices (for fields)"""
from os import path
from importlib.metadata import version as get_version, PackageNotFoundError
from setuptools.config import read_configuration

from .choices import Choices, OrderedChoices, AutoDisplayChoices, AutoChoices  # noqa: F401


def _extract_version(package_name):
    try:
        # if package is installed
        version = get_version(package_name)
    except PackageNotFoundError:
        # if not installed, so we must be in source, with ``setup.cfg`` available
        _conf = read_configuration(path.join(
            path.dirname(__file__), '..', 'setup.cfg')
        )
        version = _conf['metadata']['version']

    return version


EXACT_VERSION = _extract_version('django_extended_choices')
VERSION = tuple(int(part) for part in EXACT_VERSION.split('.') if part.isnumeric())
