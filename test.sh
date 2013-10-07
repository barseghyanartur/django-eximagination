# Core tests
./uninstall.sh
reset
./install.sh
reset
python src/eximagination/tests.py

# Django tests
pip install -r example/requirements.txt
python example/example/manage.py test eximagination