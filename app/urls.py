from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    include('api/',include('app.bitcoin.urls')),
]
