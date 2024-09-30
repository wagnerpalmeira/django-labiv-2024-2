
from django.contrib import admin
from django.urls import path, include
from promotions.views import promotions_list, promotion_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('promotions/', include('promotions.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
