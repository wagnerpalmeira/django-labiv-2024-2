from django.shortcuts import render

promotions = [
    {
        'title': 'Post Um',
        'price': 29.99,
        'url': 'https://google.com'
    },
    {
        'title': 'Robo Aspirador Kabum Smart 900',
        'price': 129.99,
        'url': 'https://www.kabum.com.br/produto/366169/robo-aspirador-kabum-smart-900-127v-branco-ir360-controle-via-app-recipiente-dispensador-de-po-kbsf011'
    },
]

def promotions_list(request):
    context  = {
        'promotions': promotions,
    }
    return render(request, 'promotions/index.html', context)


# PATH PARAM
def promotion_detail(request, pk):
    promotion = promotions[pk-1]
    return render(request, 'promotions/detail.html', {
        'promotion': promotion
    })
