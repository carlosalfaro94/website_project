from django.conf.urls import patterns, url, include


urlpatterns = patterns('',

    url(r'^sito/', include('sito.urls')), # ADD THIS NEW TUPLE!
)
