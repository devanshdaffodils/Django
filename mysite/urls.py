from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('/mjolnir', include('mjolnir.urls')),
=======
    path('',include('stormbreaker.urls')),
>>>>>>> 5f5ed4774a041e54bbe6e8951a0829418fa02dbd
]
