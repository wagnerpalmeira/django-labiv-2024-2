from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def criar_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = get_user_model()
        user_created = user.objects.create(
            email=email,
            username=username
        )

        user_created.set_password(password)

        user_created.save()

    return render(request, 'users/register.html')


def login_cliente(request):
    if request.user.is_authenticated:
        return redirect('promotions:promotions_list')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('promotions:promotions_list')
    
    return render(request, 'users/login.html')
            
def logout_user(request):
    logout(request)
    return redirect('promotions:promotions_list')


