from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('webhooks/', include('webhooks.urls')),
]
