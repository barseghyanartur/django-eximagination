__title__ = 'eximagination.exceptions'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'EximaginationException',
    'WrongImageTypeOrCantLoadTheImage',
)


class EximaginationException(Exception):
    """Base exception."""


class WrongImageTypeOrCantLoadTheImage(EximaginationException):
    """Wrong image type or can load the image exception."""

