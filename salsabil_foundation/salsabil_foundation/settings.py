"""
Django settings for salsabil_foundation project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--!68qx(&k4fho$+!@^8n16)_wz=3=8sw@rk94gvvb+)snvsqz&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CSRF_TRUSTED_ORIGINS = [
    'https://www.salsabilfoundation.com','https://salsabilfoundation.com', 'http://www.salsabilfoundation.com', 'http://salsabilfoundation.com'
]
ALLOWED_HOSTS = ['127.0.0.1', '51.20.85.244', 'www.salsabilfoundation.com', 'salsabilfoundation.com', 'https://www.salsabilfoundation.com','https://salsabilfoundation.com', 'http://www.salsabilfoundation.com', 'http://salsabilfoundation.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'charity',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'salsabil_foundation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'salsabil_foundation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'salsabilcharity',
        'USER': 'salsabilcharity',
        'PASSWORD': 'salsabilcharity$',
        'HOST': 'salsabilcharityfoundation.clkos6a8m91x.eu-north-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT= 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
PAYSTACK_SECRET_KEY = "sk_test_e3a0e8c8bc112acd10feeafab107c4e1f7432e9d"
PAYSTACK_PUBLIC_KEY = "pk_test_245070d35345896816d5f999fe01cc9261d8afc5"

AWS_ACCESS_KEY_ID = 'AKIAU5LH5QFXPZJZOIH4'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME ='salsabilcharitybucket'
AWS_S3_SIGNATURE_NAME = 's3v4'
AWS_S3_REGION_NAME = 'eu-north-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_REGION_NAME = 'eu-north-1' #(ex: us-east-2)
AWS_SES_REGION_ENDPOINT ='email.eu-north-1.amazonaws.com' #(ex: email.us-east-2.amazonaws.com)
DEFAULT_FROM_EMAIL = 'sabilcharityfoundation@gmail.com'