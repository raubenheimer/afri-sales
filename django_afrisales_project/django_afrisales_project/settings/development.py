from django_afrisales_project.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*jg(88r-i_!t$-5$y4&c80++%daq&tn+!!!0fx8tj9-!z+hv*e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1'
    ]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Afri-Sales DB', 
        'USER': 'postgres', 
        'PASSWORD': '911223344',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}