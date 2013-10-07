__title__ = 'eximagination.utils'
__version__ = '0.7'
__build__ = 0x000007
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__all__ = ('obtain_image',)

import os
import hashlib
import glob
import time
from PIL import Image

from six.moves.urllib.request import build_opener
from six import BytesIO as StringIO

def obtain_image(image_source='', save_to='', media_url='', force_update=False, expiration_interval=None, debug=False):
    """
    Gets an image from absolute url and saves it locally. Checks wheither image already exists in local directoru
    and only if not - tries to download it and saves it. Validates validity of the image (relying on PIL Image
    class validation).

    :param str image_source:
    :param str save_to:
    :param str media_url:
    :param bool force_update:
    :param int expiration_interval: Expiration interval in seconds.
    :param bool debug:
    :return list: (relative_url_of_the_image, original_image_width, original_image_height)
    """
    # First we check if any image with such name (without extention) exists in our local external images directory.
    expired = False
    try:
        filename = os.path.basename(glob.glob(os.path.join(save_to, hashlib.md5(image_source).hexdigest()) + '.*')[0])

        # Expiration interval check.
        full_path = os.path.join(save_to, filename)
        last_modified = os.path.getmtime(full_path)
        if time.time() - last_modified > expiration_interval:
            expired = True

        if not expired:
            im = Image.open(full_path) # Feed the image to PIL to get width and height
            return (os.path.join(media_url, filename), im.size[0], im.size[1])
    except Exception as e:
        pass

    # If nothing was found in local directory (or perhaps file expired) - we try to load it and save it.
    try:
        # Loading the file of unknown type into memory. We don't save the image locally before it's validated.
        opener = build_opener()
        page = opener.open(image_source)
        external_image = page.read()

        # Loading into PIL image in order to check if image is a proper image as well as to detect its' extention.
        # This is probably the best way to validate the image and get its' extention, since PIL Image throws an
        # exception when trying to load not a proper image.
        im = Image.open(StringIO(external_image))

        # This is our filename
        filename = hashlib.md5(image_source.encode('utf-8')).hexdigest() + '.' + im.format.lower()

        # If filename already exists - returning the filename
        filename_full_path = os.path.join(save_to, filename)
        if os.path.exists(filename_full_path) and os.path.isfile(filename_full_path) and not (force_update or expired):
            return (os.path.join(media_url, filename), im.size[0], im.size[1])

        # Open file for binary write and save the image.
        fout = open(filename_full_path, "wb")
        fout.write(external_image)
        fout.close()
        return (os.path.join(media_url, filename), im.size[0], im.size[1])
    except Exception as e:
        if debug:
            raise Exception("Wrong image type or can load the image")
        else:
            return ''
