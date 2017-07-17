from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('articles.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^admin/', admin.site.urls),
]
