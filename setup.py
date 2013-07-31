import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'readme.rst')).read()
except:
    readme = ''

version = '0.6'

setup(
    name = 'eximagination',
    version = version,
    description = ("Eximagination package for copying external images in tempalate tags and storing them locally."),
    long_description = readme,
    classifiers = [
        "Framework :: Django",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = 'eximagination, django, external images, app, python',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://bitbucket.org/barseghyanartur/eximagination',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
)
