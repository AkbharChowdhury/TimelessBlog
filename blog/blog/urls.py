from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

auth_url = 'django.contrib.auth.urls'
user_path = 'users/'
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('articles.urls')),
                  path(user_path, include(auth_url)),
                  path(user_path, include('users.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
