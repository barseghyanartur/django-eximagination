__title__ = 'eximagination.defaults'
__version__ = '0.6'
__build__ = 0x000006
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__all__ = ('MEDIA_ROOT', 'MEDIA_URL', 'MEDIA_RELATIVE_ROOT', 'EXPIRATION_INTERVAL', 'DEBUG')

import os
PROJECT_DIR = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')

MEDIA_ROOT = PROJECT_DIR('media/external_images') # Where eximagination cached images will be stored
MEDIA_URL = '/media/external_images/' # Media URL for stored images
MEDIA_RELATIVE_ROOT = 'external_images/' # Relative root for images
EXPIRATION_INTERVAL = 2592000 # After 30 days we re-fetch the file anyway.
DEBUG = False
