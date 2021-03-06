# -*- encoding: utf-8 -*-

# Django settings for EnceFAL project.

import os
from conf import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    # ('Nilovna Bascunan-Vasquez', 'contact@nilovna.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Montreal'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-ca'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
MEDIA_PRIVE_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_prive')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/' 

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'phgxc&v+2@4--i(t^s_d3=1w+jhw=qr*6oo2j7po(z$5*x$hup'

DEBUG=True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),],

		# automatic path searching
        'APP_DIRS': False,
        'OPTIONS': {
			# Replaces the old TEMPLATE DEBUG
			'debug': DEBUG,

            'context_processors': [
				'django.contrib.auth.context_processors.auth',
               	'django.template.context_processors.debug',
				'django.template.context_processors.i18n',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
				'django.template.context_processors.tz',
      			'django.template.context_processors.request', 					'django.contrib.messages.context_processors.messages',
            ],

			# Replaces TEMPLATE LOADERS
			'loaders': [
            	#'django.template.loaders.cached.Loader',
 					'django.template.loaders.filesystem.Loader',              					'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

STATIC_ROOT = os.path.join(BASE_DIR,'project', 'encefal', 'static')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

BOOTSTRAP3 = {
	'base_url': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/'
}

ROOT_URLCONF = 'project.urls'

LOGIN_REDIRECT_URL = "/employee/"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'bootstrap_toolkit',
    'project.encefal',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'south',
)

STATIC_URL = '/static/'
