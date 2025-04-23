"""
WSGI config for ISTP_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from pathlib import Path

# Add the project directory to the sys.path
path_home = str(Path(__file__).parent.parent)
if path_home not in sys.path:
    sys.path.append(path_home)

# Add the parent directory to the sys.path
path_parent = str(Path(__file__).parent.parent.parent)
if path_parent not in sys.path:
    sys.path.append(path_parent)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ISTP_website.settings')

application = get_wsgi_application()

# For gunicorn
app = application
