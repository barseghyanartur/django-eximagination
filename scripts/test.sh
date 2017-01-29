reset
#./scripts/uninstall.sh
#./scripts/install.sh
#python examples/simple/manage.py test dummy_thumbnails --traceback -v 3 --settings=settings.testing

# Core tests
./scripts/uninstall.sh
reset
#./scripts/install.sh
reset
python src/eximagination/tests.py

# Django tests
pip install -r examples/requirements.txt
python examples/simple/manage.py test eximagination