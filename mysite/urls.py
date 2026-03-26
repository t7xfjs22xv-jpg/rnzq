from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.admin_urls),
    path('', include('petal.urls')), # This connects everything
]