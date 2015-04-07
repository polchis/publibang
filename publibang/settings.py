#encoding:utf-8
"""
Django settings for publibang project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y^l7%z-+fzpe4^=k*s(^z97q(wq+tktgd8@jh3y1kw!#b9*$6r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

MEDIA_ROOT = '/home/polchis/entornos/hyoclub/publibang/publibang/media/'
MEDIA_URL = 'http://localhost:8000/media/'


TEMPLATE_DIRS = (
        os.path.join(os.path.dirname(__file__), 'template').replace('\\','/'),
    )

STATICFILES_DIRS = (
        os.path.join(os.path.dirname(__file__), 'static').replace('\\','/'),
    )

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'security',
    'star',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'publibang.urls'

WSGI_APPLICATION = 'publibang.wsgi.application'

CONCURSO = 1

ADFLY_API = "http://api.adf.ly/api.php?key=a5c83f8ec8c3be3222cf19b6243343ce&uid=9486419&advert_type=int&domain=adf.ly&url="

URL_RECIVE = ADFLY_API + "http://hyo.club/participa/recibir/?"

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'publibang.db',
        'USER': 'root',
        'PASSWORD': 'toor',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
