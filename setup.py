import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

version = '0.7'

setup(
    name = 'eximagination',
    version = version,
    description = (
        "A Django template tag library which allows to download external images, store them locally "
        "and return the local path to locally stored image to a desired context variable"
        ),
    long_description = readme,
    classifiers = [
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    keywords = 'eximagination, django, external images, app, python',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://github.com/barseghyanartur/eximagination',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
    install_requires = [
        'six==1.4.1',
        'Pillow==2.2.1'
    ]
)
