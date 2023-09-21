"""
URL patterns for the views included in ``django.contrib.auth``.

Including these URLs (via the ``include()`` directive) will set up the
following patterns based at whatever URL prefix they are included
under:

* User login at ``login/``.

* User logout at ``logout/``.

* The two-step password change at ``password/change/`` and
  ``password/change/done/``.

* The four-step password reset at ``password/reset/``,
  ``password/reset/confirm/``, ``password/reset/complete/`` and
  ``password/reset/done/``.

The default registration backend already has an ``include()`` for
these URLs, so under the default setup it is not necessary to manually
include these views. Other backends may or may not include them;
consult a specific backend's documentation for details.

"""

from django.contrib.auth import views as auth_views
from django.urls import re_path

from django_facebook import registration_views
from django_facebook.utils import replication_safe

urlpatterns = [
    re_path(
        r'^login/$',
        replication_safe(auth_views.login),
        {'template_name': 'registration/login.html'},
        name='auth_login'
    ),
    re_path(
        r'^logout/$',
        replication_safe(auth_views.logout),
        {'template_name': 'registration/logout.html'},
        name='auth_logout'
    ),
    re_path(
        r'^password/change/$',
        auth_views.password_change,
        name='auth_password_change'
    ),
    re_path(
        r'^password/change/done/$',
        auth_views.password_change_done,
        name='auth_password_change_done'
    ),
    re_path(
        r'^password/reset/$',
        auth_views.password_reset,
        name='auth_password_reset'
    ),
    re_path(
        r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='auth_password_reset_confirm'
    ),
    re_path(
        r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='auth_password_reset_complete'
    ),
    re_path(
        r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='auth_password_reset_done'
    ),
    re_path(
        r'^register/$',
        registration_views.register,
        name='registration_register'
    ),
]
