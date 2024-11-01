from django.urls import path
from promotions.views import PromotionListView, promotion_detail, create_promotion

app_name = 'promotions'

urlpatterns = [
    path('', PromotionListView.as_view(), name='promotions_list'),
    path('create/', create_promotion, name='promotions_create'),
    path('<int:pk>/', promotion_detail, name='promotion_detail'),
]
