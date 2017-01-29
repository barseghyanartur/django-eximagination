pip uninstall eximagination -y
pip uninstall django-eximagination -y
rm build -rf
rm dist -rf
rm -rf src/django-eximagination.egg-info
rm -rf src/django_eximagination.egg-info
rm -rf src/eximagination.egg-info
./scripts/clean_up.sh
