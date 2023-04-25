from .settings import *
from django.urls import include, path

globals().setdefault('DEBUG', False)

if DEBUG:
    INSTALLED_APPS += [
        'django_extensions',
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = [
        '127.0.0.1',
    ]

    DEV_URLS = [
        path('__debug__/', include("debug_toolbar.urls")),
    ]
