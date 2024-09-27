from django.shortcuts import render
from promotions.models.promotion import Promotion

def promotions_list(request):
    promotions = Promotion.objects.all()
    context  = {
        'promotions': promotions,
    }
    return render(request, 'promotions/index.html', context)


# PATH PARAM
def promotion_detail(request, pk):
    promotion = Promotion.objects.get(pk=pk)
    return render(request, 'promotions/detail.html', {
        'promotion': promotion
    })
