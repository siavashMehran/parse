
from os import path, environ
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = environ.get('SECRET_KEY', '#fqw4&9shg@ewv-ar(jh2fm%*4pk6vq9+(ln@%1d6^0!5pod5x')


DEBUG = environ.get('DEBUG', True)

ALLOWED_HOSTS = [
    'gardeshgaranparseh.com',
    'http://gardeshgaranparseh.com',
    'https://gardeshgaranparseh.com',
]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #third party
    'rest_framework',
    'django_render_partial',
    'tinymce',

    #apps
    'APP_INFO',
    'APP_TOUR',
    'partials'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


if DEBUG == False:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True





STATIC_URL  = '/static/'
STATIC_ROOT = path.join(BASE_DIR, 'storage', 'STATIC')
STATICFILES_DIRS = [path.join(BASE_DIR, 'assets')]

MEDIA_URL  = '/user/'
MEDIA_ROOT = path.join(BASE_DIR, 'storage', 'MEDIA')

# AUTH_USER_MODEL = 'VEGAN_API_ACCOUNT.User'
# LOGIN_URL = '/account/'

DEFAULT_CHARSET = 'UTF-8'

LANGUAGES = (
    ('fa', 'farsi'),
    ('en', 'english'),
)

if DEBUG :


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


    INSTALLED_APPS += [
        # 'debug_toolbar',
    ]

    ALLOWED_HOSTS += [ 
        'localhost'
    ]
    # debug_toolbar
    INTERNAL_IPS = [
        '127.0.0.1',
        'localhost',
        
    ]