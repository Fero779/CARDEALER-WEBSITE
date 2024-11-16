"""
WSGI config for cardealer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Ensure the correct settings module is loaded based on the environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cardealer.settings')

# For Heroku, you can use 'django_heroku' for proper configuration
import django_heroku

# Apply Heroku-specific settings after loading the settings
application = get_wsgi_application()
django_heroku.settings(locals())  # This ensures Heroku settings are applied
