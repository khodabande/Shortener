from django.conf.urls import url

from .views import shortener_redirect_view

urlpatterns = [
    url(r'^(?P<slug>.*)/$', shortener_redirect_view, name='shortener_redirect_view'),
]

