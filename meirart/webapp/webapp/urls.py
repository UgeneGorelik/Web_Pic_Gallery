from django.contrib import admin
from django.urls import path,utils,include
from django.conf.urls import url
from . views import login_redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',login_redirect,name='login_redirect'),
    path('admin/', admin.site.urls),
    url(r'^gallery/',include('gallery.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)