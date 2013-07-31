__title__ = 'eximagination.utils'
__version__ = '0.6'
__build__ = 0x000006
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__all__ = ('_obtain_image',)

import urllib2
import os
import hashlib
from PIL import Image
import StringIO
import glob
import time

from eximagination.settings import EXPIRATION_INTERVAL, DEBUG

def _obtain_image(image_source='', save_to='', media_url='', force_update=False):
    """
    Gets an image from absolute url and saves it locally. Checks wheither image already exists in local directoru
    and only if not - tries to download it and saves it. Validates validity of the image (relying on PIL Image
    class validation).

    :param image_source: str
    :param save_to: str
    :param media_url: str
    :param force_update: bool
    :return list: (relative_url_of_the_image, original_image_width, original_image_height)
    """
    # First we check if any image with such name (without extention) exists in our local external images directory.
    expired = False
    try:
        filename = os.path.basename(glob.glob(os.path.join(save_to, hashlib.md5(image_source).hexdigest()) + '.*')[0])

        # Expiration interval check.
        full_path = os.path.join(save_to, filename)
        last_modified = os.path.getmtime(full_path)
        if time.time() - last_modified > EXPIRATION_INTERVAL:
            expired = True

        if not expired:
            im = Image.open(full_path) # Feed the image to PIL to get width and height
            return (os.path.join(media_url, filename), im.size[0], im.size[1])
    except Exception, e:
        pass

    # If nothing was found in local directory (or perhaps file expired) - we try to load it and save it.
    try:
        # Loading the file of unknown type into memory. We don't save the image locally before it's validated.
        opener = urllib2.build_opener()
        page = opener.open(image_source)
        external_image = page.read()

        # Loading into PIL image in order to check if image is a proper image as well as to detect its' extention.
        # This is probably the best way to validate the image and get its' extention, since PIL Image throws an
        # exception when trying to load not a proper image.
        im = Image.open(StringIO.StringIO(external_image))

        # This is our filename
        filename = hashlib.md5(image_source).hexdigest() + '.' + im.format.lower()

        # If filename already exists - returning the filename
        filename_full_path = os.path.join(save_to, filename)
        if os.path.exists(filename_full_path) and os.path.isfile(filename_full_path) and not (force_update or expired):
            return (os.path.join(media_url, filename), im.size[0], im.size[1])

        # Open file for binary write and save the image.
        fout = open(filename_full_path, "wb")
        fout.write(external_image)
        fout.close()
        return (os.path.join(media_url, filename), im.size[0], im.size[1])
    except Exception, e:
        if DEBUG:
            raise Exception("Wrong image type or can load the image")
        else:
            return ''
