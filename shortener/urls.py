from django.conf.urls import patterns, url

urlpatterns = patterns('shortener.views',
    url(r'^(?P<slug>.*)/$', 'shortener_redirect_view', name='shortener_redirect_view'),
)
