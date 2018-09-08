from .common import *

DEBUG = True

ALLOWED_HOSTS = []

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
