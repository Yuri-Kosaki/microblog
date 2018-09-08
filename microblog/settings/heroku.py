from .common import *

DEBUG = False

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_ROOT = 'staticfiles'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'microblog',   # DB名を設定（変更可）
        'USER': 'root',       # DBへ接続するユーザIDを設定（rootはあまりよろしくない）
        'PASSWORD': '',       # DBへ接続するユーザIDのパスワードを設定
        'HOST': 'localhost',
        'PORT': '3306',
        'TEST': {
            'NAME': 'sample'
        }
    }
}

try:
    from .local_settings import *
except ImportError:
    pass
