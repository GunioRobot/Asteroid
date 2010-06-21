import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
sys.stdout = sys.stderr
os.environ['DJANGO_SETTINGS_MODULE'] = 'runner.settings'
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()