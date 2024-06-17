from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('setup.urls')),
    path('blog/', include('blog.urls')),
    path('home/', include('home.urls')),
]
