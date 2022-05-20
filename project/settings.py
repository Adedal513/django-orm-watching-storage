import os
from os import path

from dotenv import load_dotenv
from environs import Env


load_dotenv()
env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env.str('DB_ENGINE'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.str('DEBUG') in ['True', 'true', 'TRUE']

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list(name='ALLOWED_HOSTS', subcast=str, separator=',')

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
