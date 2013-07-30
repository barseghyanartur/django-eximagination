__title__ = 'eximagination.conf'
__version__ = '0.5'
__build__ = 0x000005
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__all__ = ('get_setting',)

from django.conf import settings

from eximagination import defaults

def get_setting(setting, override=None):
    """
    Get a setting from eximagination conf module, falling back to the default.

    If override is not None, it will be used instead of the setting.

    There are some app settings you may want to override. You can override any of the following default settings in
    your project settings module:

        `MEDIA_ROOT`

        `MEDIA_URL`

        `MEDIA_RELATIVE_ROOT`

    :param str setting: Name of the setting.
    :param override: Default value
    :return: Desired setting value

    :example:
    >>> from eximagination.conf import get_setting
    >>> MEDIA_ROOT = get_setting('MEDIA_ROOT')
    """
    if override is not None:
        return override
    if hasattr(settings, 'EXIMAGINATION_%s' % setting):
        return getattr(settings, 'EXIMAGINATION_%s' % setting)
    else:
        return getattr(defaults, setting)
