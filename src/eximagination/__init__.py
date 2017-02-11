"""
A Django template tag library which allows to download external images, store
them locally and return the local path to locally stored image to a desired
context variable, along with `width` and `height` of the image fetched. Caches
the fetched images locally for the given time (set in settings). You could,
for example, use this app to solve the problems with displaying of a mixed
content (assets loaded from HTTP and HTTPS sources).

- default_app_config: Default Django app config.
"""

from .utils import obtain_image

__title__ = 'eximagination'
__version__ = '0.8.1'
__build__ = 0x000009
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'obtain_image',
    'default_app_config',
)

default_app_config = 'eximagination.apps.Config'
