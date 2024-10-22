from django.urls import path
from promotions.views import promotions_list, promotion_detail, create_promotion

app_name = 'promotions'

urlpatterns = [
    path('', promotions_list, name='promotions_list'),
    path('create/', create_promotion, name='promotions_create'),
    path('<int:pk>/', promotion_detail, name='promotion_detail'),
]
