from django.urls import re_path
from django.conf.urls import include
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # facebook and registration urls
    re_path(r'^facebook/', include('django_facebook.urls')),
    re_path(r'^accounts/', include('django_facebook.auth_urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    re_path(r'^admin/', include(admin.site.urls)),
]

if settings.MODE == 'userena':
    urlpatterns += [
        re_path(r'^accounts/', include('userena.urls')),
    ]
elif settings.MODE == 'django_registration':
    urlpatterns += [
        re_path(r'^accounts/', include('registration.backends.default.urls')),
    ]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
        ]
