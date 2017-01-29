from .helpers import project_dir

__title__ = 'eximagination.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'MEDIA_ROOT',
    'MEDIA_URL',
    'MEDIA_RELATIVE_ROOT',
    'EXPIRATION_INTERVAL',
    'DEBUG'
)

# Where eximagination cached images will be stored
MEDIA_ROOT = project_dir('media/external_images')
MEDIA_URL = '/media/external_images/'  # Media URL for stored images
MEDIA_RELATIVE_ROOT = 'external_images/'  # Relative root for images
EXPIRATION_INTERVAL = 2592000  # After 30 days we re-fetch the file anyway.
DEBUG = False
