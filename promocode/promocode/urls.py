
from django.contrib import admin
from django.urls import path
from promotions.views import promotions_list, promotion_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('promotions/', promotions_list),
    path('promotions/<int:pk>/', promotion_detail)
    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
