from django.shortcuts import render

def promotions_list(request):
    return render(request, 'promotions/index.html')
