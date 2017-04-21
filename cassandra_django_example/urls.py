from django.conf.urls import url, include
from django.contrib import admin

from comments import urls as comments_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'comments/', include(comments_urls))
]
