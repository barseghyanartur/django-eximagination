=======================================
eximagination
=======================================

Description
=======================================
A Django template tag library which allows downloading of external images right from the template and save it into a
desired context variable along with `width` and `height` of the image fetched. Caches the fetched images locally.
You could, for example, use this app to solve the problems with displaying of a mixed content (assets loaded from HTTP and HTTPS
sources).

Installation
=======================================
1. Install eximagination

Latest stable version on PyPI:

    $ pip install eximagination

Latest development version from source:

    $ pip install -e hg+http://bitbucket.org/barseghyanartur/eximagination@dev#egg=eximagination

2. Add 'eximagination' to `INSTALLED_APPS`

>>> INSTALLED_APPS = (
>>>     # ...
>>>     'eximagination',
>>>     # ...
>>> )

3. Configure

By default, eximagination expects your files to be stored in '/media/external_images' directory. If location varies,
redefine the directories in your Django settings, make sure the path is writable and that www-data (or whatever is
applicable) has rights to write into it.

>>> # Example settings.py
>>> import os
>>> PROJECT_DIR = lambda s: os.path.abspath(os.path.join(os.path.dirname(__file__), s).replace('\\','/'))
>>> EXIMAGINATION_MEDIA_ROOT = PROJECT_DIR('media/external_images/')
>>> EXIMAGINATION_MEDIA_URL = '/media/external_images'
>>> EXIMAGINATION_MEDIA_RELATIVE_ROOT = 'external_images/'
>>> EXIMAGINATION_DEBUG = True

Usage example (in a Django template)
=======================================
See the `example` directory in https://bitbucket.org/barseghyanartur/eximagination/src for working code example.

{% load eximaginate %}

<img src="{{ MEDIA_URL }}{% eximaginate 'http://www.google.com/intl/en/images/logo.gif' %}">

or

{% load eximaginate thumbnail %}

{% eximaginate 'http://www.google.com/intl/en/images/logo.gif' as original %}

<img src="{% thumbnail original 100x100 %}">

In both cases there are two additional context variables added:

    `ei_width` - Width of the image

    `ei_height` - Height of the image

License
=======================================
GPL 2.0/LGPL 2.1

Support
=======================================
For any issues contact me at the e-mail given in the `Author` section or open an issue on bitbucket/github.

Author
=======================================
Artur Barseghyan <artur.barseghyan@gmail.com>
