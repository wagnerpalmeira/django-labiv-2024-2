
from django.contrib import admin
from django.urls import path
from promotions.views import promotions_list

urlpatterns = [
    path('promotions/', promotions_list),
    # path('admin/', admin.site.urls),
]
