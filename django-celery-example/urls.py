from django.conf.urls import include, url
from django.contrib import admin
from core.views import *

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^generate/$', GenerateRandomUserView.as_view(), name="contraparte-list"),


    url(r'^books/$', view_books),
    url(r'^books/cache/', view_cached_books),
]
