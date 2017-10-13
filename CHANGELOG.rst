Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.8.3
-----
2017-10-14

- Added ``get_new_image_filename`` for getting the filename of the image to
  created.

0.8.2
-----
2017-10-14
- Added Exceptions.

0.8.1
-----
2017-01-29

- Tested against Python 3.6 and Django 1.11.

0.8
---
2017-01-29

- Made compatible with Django 1.8, 1.9, 1.10. Drop support for older Django
  versions. Drop support for Python 2.6.
- Changed package version from ``eximagination`` to ``django-eximagination``.
- Wheel support.
