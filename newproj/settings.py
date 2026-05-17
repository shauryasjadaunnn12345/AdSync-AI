import os
import environ
import dj_database_url
from pathlib import Path

# Initialize environment variables
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# ========================
# SECURITY
# ========================
SECRET_KEY = env('SECRET_KEY', default='django-insecure-dev-key')
DEBUG =True
ALLOWED_HOSTS =['*']

# ========================
# APPLICATIONS
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',  # Required for Supabase Storage
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'newproj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'newproj.wsgi.application'

# ========================
# DATABASE (SUPABASE)
# ========================
DATABASES = {
    'default': dj_database_url.parse(
        env('SUPABASE_DB_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# ========================
# MEDIA FILES (SUPABASE STORAGE)
# ========================

# Get Supabase details
SUPABASE_URL = env('SUPABASE_URL', default=None)
SUPABASE_KEY = env('SUPABASE_SERVICE_KEY', default=None)
SUPABASE_BUCKET = env('SUPABASE_BUCKET', default=None)
# OLD WAY
# environ.Env.read_env() 

# NEW WAY (Remove read_env, just initialize)
env = environ.Env()

# ... existing code ...

# Explicitly load from OS Environment
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG', default=False)
MISTRAL_API_KEY = env('MISTRAL_API_KEY') 
SUPABASE_URL = env('SUPABASE_URL', default=None)
# ... etc
if SUPABASE_URL and SUPABASE_KEY:
    # We configure the S3 backend to point to Supabase
    # This maps your Supabase credentials to the S3 protocol
    
    # The internal storage library needs these specific variable names
    AWS_S3_ENDPOINT_URL = f"{SUPABASE_URL}/storage/v1/s3"
    AWS_ACCESS_KEY_ID = SUPABASE_KEY
    AWS_SECRET_ACCESS_KEY = SUPABASE_KEY
    AWS_STORAGE_BUCKET_NAME = SUPABASE_BUCKET
    AWS_S3_REGION_NAME = 'us-east-1' # Default required, but endpoint URL overrides it
    AWS_S3_ADDRESSING_STYLE = 'virtual'

    # This ensures files are publicly viewable without signing
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    # Define the Public URL for the frontend
    # Format: https://project-ref.supabase.co/storage/v1/object/public/bucket/
    MEDIA_URL = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/"
    
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

else:
    # LOCAL FALLBACK
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

# ========================
# STATIC FILES (Local)
# ========================
# Keeping static files local for simplicity in this setup
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# ========================
# OTHER SETTINGS
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MISTRAL_API_KEY = env('MISTRAL_API_KEY')
