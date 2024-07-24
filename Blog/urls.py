from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page for the blog portal
    path('', include('ygyBlog.urls')),
    # Login or register page for the website
    path('auth/', include('ygyAuth.urls')),
]
