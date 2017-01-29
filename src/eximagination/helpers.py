import os

__title__ = 'eximagination.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'project_dir',
    'PROJECT_DIR',
)


def project_dir(base):
    """Get path to directory/file from current path."""
    return os.path.join(os.path.dirname(__file__), base).replace('\\', '/')


PROJECT_DIR = project_dir
