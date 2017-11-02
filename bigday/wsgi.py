"""
WSGI config for bigday project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/data/www/multiplace.org/mara@multiplace.org/greek-wedding')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigday.settings")

application = get_wsgi_application()
