from django.urls import path
from promotions.views import promotions_list, promotion_detail

app_name = 'promotions'

urlpatterns = [
    path('', promotions_list, name='promotions_list'),
    path('<int:pk>/', promotion_detail, name='promotion_detail'),
]
