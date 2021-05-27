from django_afrisales_project.settings.common import *
import django_heroku


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'afri-sales.herokuapp.com'
    ]

django_heroku.settings(locals())