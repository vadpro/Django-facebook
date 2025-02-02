from django.conf import settings

# help autodiscovery a bit
from django.urls import re_path

from django_facebook import admin
from .views import connect, disconnect, example
from .example_views import *

urlpatterns = [
    re_path(r'^connect/$', connect, name='facebook_connect'),
    re_path(r'^disconnect/$',
        disconnect, name='facebook_disconnect'),
    re_path(r'^example/$', example, name='facebook_example'),
]

dev_patterns = [
    re_path(
        r'^lazy_decorator_example/$', lazy_decorator_example,
        name='facebook_lazy_decorator_example'),
    re_path(r'^decorator_example/$', decorator_example,
        name='facebook_decorator_example'),
    re_path(
        r'^decorator_example_scope/$', decorator_example_scope,
        name='facebook_decorator_example_scope'),
    re_path(r'^wall_post/$',
        wall_post, name='facebook_wall_post'),
    re_path(r'^checkins/$',
        checkins, name='facebook_checkins'),
    re_path(r'^image_upload/$',
        image_upload, name='facebook_image_upload'),
    re_path(r'^canvas/$', canvas, name='facebook_canvas'),
    re_path(r'^page_tab/$',
        page_tab, name='facebook_page_tab'),
    re_path(r'^open_graph_beta/$', open_graph_beta,
        name='facebook_open_graph_beta'),
    re_path(r'^remove_og_share/$', remove_og_share,
        name='facebook_remove_og_share'),
]

# when developing enable the example views
if settings.DEBUG or getattr(settings, 'TESTING', False):
    # only enable example views while developing
    urlpatterns += dev_patterns


# putting this here instead of models.py reduces issues with import ordering
if getattr(settings, 'AUTH_PROFILE_MODULE', None) == 'django_facebook.FacebookProfile':
    '''
    If we are using the django facebook profile model, create the model
    and connect it to the user create signal
    '''

    from django.db.models.signals import post_save
    from django_facebook.models import FacebookProfile
    from django_facebook.utils import get_user_model

    # Make sure we create a FacebookProfile when creating a User
    def create_facebook_profile(sender, instance, created, **kwargs):
        if created:
            FacebookProfile.objects.create(user=instance)

    post_save.connect(create_facebook_profile, sender=get_user_model())
