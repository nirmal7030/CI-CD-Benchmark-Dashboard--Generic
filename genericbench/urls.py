from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Make the generic dashboard the main entry or under /generic/
    path('', include('metrics.urls')),          # root → generic dashboard
    # or alternatively:
    # path('generic/', include('metrics.urls')),
]
