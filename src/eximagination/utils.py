import os
import hashlib
import glob
import time

from six.moves.urllib.request import build_opener
from six import BytesIO as StringIO

try:
    from PIL import Image
except ImportError:
    import Image

__title__ = 'eximagination.utils'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('obtain_image',)


def obtain_image(image_source='', save_to='', media_url='',
                 force_update=False, expiration_interval=None, debug=False):
    """Get an image from absolute url and saves it locally.

    Check whether image already exists in local directory and only if not -
    try to download it and save it. Validate validity of the image (rely on
    PIL Image class validation).

    :param str image_source:
    :param str save_to:
    :param str media_url:
    :param bool force_update:
    :param int expiration_interval: Expiration interval in seconds.
    :param bool debug:
    :return list: (relative_url_of_the_image,
                   original_image_width,
                   original_image_height)
    """
    # First we check if any image with such name (without extention) exists
    # in our local external images directory.
    expired = False
    try:
        filename = os.path.basename(
            glob.glob(
                os.path.join(
                    save_to,
                    hashlib.md5(image_source).hexdigest()
                ) + '.*'
            )[0]
        )

        # Expiration interval check.
        full_path = os.path.join(save_to, filename)
        last_modified = os.path.getmtime(full_path)
        if time.time() - last_modified > expiration_interval:
            expired = True

        if not expired:
            # Feed the image to PIL to get width and height
            img = Image.open(full_path)
            return os.path.join(media_url, filename), img.size[0], img.size[1]
    except Exception:
        pass

    # If nothing was found in local directory (or perhaps file expired) - we
    # try to load it and save it.
    try:
        # Loading the file of unknown type into memory. We don't save the
        # image locally before it's validated.
        opener = build_opener()
        page = opener.open(image_source)
        external_image = page.read()

        # Loading into PIL image in order to check if image is a proper image
        # as well as to detect its' extension. This is probably the best way
        # to validate the image and get its' extension, since PIL Image throws
        # an exception when trying to load not a proper image.
        img = Image.open(StringIO(external_image))

        # This is our filename
        filename = hashlib.md5(
            image_source.encode('utf-8')
        ).hexdigest() + '.' + img.format.lower()

        # If filename already exists - returning the filename
        filename_full_path = os.path.join(save_to, filename)
        if os.path.exists(filename_full_path) \
                and os.path.isfile(filename_full_path) \
                and not (force_update or expired):
            return os.path.join(media_url, filename), img.size[0], img.size[1]

        # Open file for binary write and save the image.
        fout = open(filename_full_path, "wb")
        fout.write(external_image)
        fout.close()
        return os.path.join(media_url, filename), img.size[0], img.size[1]
    except Exception:
        if debug:
            raise Exception("Wrong image type or can load the image")
        else:
            return ''
