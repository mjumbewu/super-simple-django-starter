import os
import sys

BASE_PATH = os.path.dirname(__file__)

from django.conf import settings
from django.conf.urls import patterns
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    SECRET_KEY='placerandomsecretkeyhere',
    ROOT_URLCONF=sys.modules[__name__],
)

def index(request):
    return HttpResponse('Powered by Django')

urlpatterns = patterns('',
    (r'^$', index),
)

application = get_wsgi_application()

if __name__ == "__main__":
    execute_from_command_line(sys.argv)