# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.conf import settings

from runner.views import run_command, show_command, list_commands, show_run, \
    dashboard, list_runs, run_web_hook

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^$', dashboard),
    (r'^commands/$', list_commands),
    (r'^runs/$', list_runs),
    (r'^commands/(?P<command>[-\w]+)/(?P<run>\d+)/$', show_run),
    (r'^commands/(?P<command>[-\w]+)/run/$', run_command),
    (r'^commands/(?P<command>[-\w]+)/(?P<run>\d+)/hook/$', run_web_hook),
    (r'^commands/(?P<command>[-\w]+)/$', show_command),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),

    # copied from django.contrib.auth
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout'),
    (r'^auth/password_change/$', 'django.contrib.auth.views.password_change'),
    (r'^auth/password_change/done/$', 'django.contrib.auth.views.password_change_done'),
    (r'^auth/password_reset/$', 'django.contrib.auth.views.password_reset'),
    (r'^auth/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^auth/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^auth/reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

)