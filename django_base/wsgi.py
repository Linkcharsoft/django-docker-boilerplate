"""
WSGI config for django_base project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
from django_base.settings import IS_SERVER
import os
from django.core.wsgi import get_wsgi_application

if IS_SERVER:
    import time
    import traceback
    import signal
    import sys

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_base.settings'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_base.settings")
    try:
        application = get_wsgi_application()
    except Exception:
        # Error loading applications 
        if 'mod_wsgi' in sys.modules:
            traceback.print_exc()
            os.kill(os.getpid(), signal.SIGINT)
        
            time.sleep(2.5)
    
else:   
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_base.settings')

    application = get_wsgi_application()