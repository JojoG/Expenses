dependencies:

django-registration (from bitbucket)
django-profiles
south
django-devserver https://github.com/dcramer/django-devserver {
pip install git+git://github.com/dcramer/django-devserver#egg=django-devserver
pip install sqlparse
pip install werkzeug
pip install https://guppy-pe.svn.sourceforge.net/svnroot/guppy-pe/trunk/guppy
pip install line_profiler
}



in the main directory (here), create a constants.py file:::


DOMAIN = 'localhost:8000'
ADMIN_UN = <admin un>
ADMIN_UE = <email>
ADMIN_PW = <pw>
DB_ENGINE = 'sqlite3' # mysql
DB_NAME = 'Expenses.db'
DB_USER = ''
DB_PASSWORD = ''
DB_HOST = localhost
DB_PORT =  3306
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT =  587
EMAIL_HOST_USER = <un> 
EMAIL_HOST_PASSWORD = <pw> 
EMAIL_USE_TLS = True
