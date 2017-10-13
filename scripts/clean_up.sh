find . -name "*.pyc" -exec rm -rf {} \;
find . -name "__pycache__" -exec rm -rf {} \;
find . -name "*.orig" -exec rm -rf {} \;
rm -rf build/
rm -rf dist/
rm -rf src/django-eximagination.egg-info
rm -rf src/django_eximagination.egg-info
rm -rf src/eximagination.egg-info
rm -rf .cache/
