from pathlib import Path
import os

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING
SECRET_KEY = 'django-insecure-&-$wm3&s4&%q3gab+=9#ihiqch--k=(xufn)&(*#r7fpun9yex'

DEBUG = True

ALLOWED_HOSTS = [
    "car-store-1lom.onrender.com",
    "localhost",
    "127.0.0.1",
]



# ========================
# Applications
# ========================

INSTALLED_APPS = [
    'detail_selling_app',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]


# ========================
# Middleware
# ========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]


# ========================
# URL / WSGI (THIS WAS THE BUG)
# ========================

ROOT_URLCONF = 'detail_selling.urls'

WSGI_APPLICATION = 'detail_selling.wsgi.application'


# ========================
# Templates
# ========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ========================
# Database
# ========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ========================
# Password validation
# ========================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)


# ========================
# Internationalization
# ========================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

CSRF_TRUSTED_ORIGINS = [
    "https://car-store-1lom.onrender.com",
]

# ========================
# Static & Media
# ========================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ========================
# Auth / Allauth
# ========================

SITE_ID = 1

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = ''
LOGOUT_REDIRECT_URL = 'login'

ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"

ACCOUNT_LOGOUT_ON_GET = True
SOCIALACCOUNT_LOGIN_ON_GET = True


# ========================
# Messages
# ========================

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}


# ========================
# Email (⚠️ move to env vars later)
# ========================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'shmakeyh12@gmail.com'
EMAIL_HOST_PASSWORD = 'harhsvkwbynumtru'

CSRF_TRUSTED_ORIGINS = [  
    "https://car-store-1lom.onrender.com",
]
# ========================
# Default PK
# ========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
