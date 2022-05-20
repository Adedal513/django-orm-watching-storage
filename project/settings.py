from os import getenv, path

from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': getenv('DB_ENGINE'),
        'HOST': getenv('DB_HOST'),
        'PORT': getenv('DB_PORT'),
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_USER'),
        'PASSWORD': getenv('DB_PASSWORD'),
    }
}


INSTALLED_APPS = ['datacenter']

SECRET_KEY = getenv('SECRET_KEY')

DEBUG = getenv('DEBUG') in ['True', 'true', 'TRUE']

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
