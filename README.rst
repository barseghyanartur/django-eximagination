====================
django-eximagination
====================
Fetch external images directly from templates.

A Django template tag library which allows to download external images, store
them locally and return the local path to locally stored image to a desired
context variable, along with ``width`` and ``height`` attributes of the image
fetched. Caches the fetched images locally for the given time (set in
settings).

You could, for example, use this app to solve the problems with displaying of
a mixed content (assets loaded from HTTP and HTTPS sources).

Prerequisites
=============
- Django 1.8, 1.9, 1.10
- Python >=2.7, >=3.4

Installation
============
1. Install ``django-eximagination``

Latest stable version on PyPI:

.. code-block:: sh

    pip install django-eximagination

Latest stable version from GitHub:

    pip install https://github.com/barseghyanartur/django-eximagination/archive/stable.tar.gz

2. Add ``eximagination`` to ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'eximagination',
        # ...
    )

3. Configure

By default, ``django-eximagination`` expects your files to be stored in
``/media/external_images`` directory. If location varies, redefine the
directories in your Django settings, make sure the path is writable and that
www-data (or whatever is applicable) has rights to write into it.

.. code-block:: python

    import os

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')
    EXIMAGINATION_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'external_images')
    EXIMAGINATION_MEDIA_URL = '/media/external_images'
    EXIMAGINATION_MEDIA_RELATIVE_ROOT = 'external_images/'
    # After 30 days we re-fetch the file anyway.
    EXIMAGINATION_EXPIRATION_INTERVAL = 2592000

Usage example (in a Django template)
====================================
See the `example directory
<https://bitbucket.org/barseghyanartur/django-eximagination/src>`_ for working
code example.

Example #1:

.. code-block:: html

    {% load eximaginate %}

    <img src="{{ MEDIA_URL }}{% eximaginate 'http://www.google.com/intl/en/images/logo.gif' %}">

Example #2:

.. code-block:: html

    {% load eximaginate thumbnail %}

    {% eximaginate 'http://www.google.com/intl/en/images/logo.gif' as original %}

    <img src="{% thumbnail original 100x100 %}">

In both cases there are two additional context variables added:

- ``ei_width`` - Width of the image
- ``ei_height`` - Height of the image

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section or open
an issue on BitBucket/GitHub.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
