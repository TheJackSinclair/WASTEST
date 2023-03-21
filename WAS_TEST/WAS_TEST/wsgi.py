"""
WSGI config for WAS_TEST project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAS_TEST.settings')

# application = get_wsgi_application()

import os
import sys
path = os.path.expanduser('~/WAS_TEST/')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'WAS_TEST.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()