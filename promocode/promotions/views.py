from django.shortcuts import render, redirect
from promotions.models.promotion import Promotion
from .forms import CreatePromotionForm

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

def create_promotion(request):
    if request.method == 'POST':
        promotion_form = CreatePromotionForm(request.POST)
        if promotion_form.is_valid():
            promotion = promotion_form.save(commit=False)
            promotion.user = request.user
            promotion.save()
            return redirect('promotions:promotions_list')
    promotion_form = CreatePromotionForm()

    return render(request, 'promotions/create.html', {
        'form': promotion_form
    })
