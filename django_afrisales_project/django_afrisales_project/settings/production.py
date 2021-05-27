from django_afrisales_project.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*jg(88r-i_!t$-5$y4&c80++%daq&tn+!!!0fx8tj9-!z+hv*e'
os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'afri-sales.herokuapp.com'
    ] 