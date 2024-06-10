from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout

def register_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('autenticacao:login_view')

    return render(request, 'autenticacao/register.html')

def login_view(request):

    if request.method == "GET" and 'HTTP_REFERER' in request.META:
        request.session['login_referer'] = request.META['HTTP_REFERER']

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            # Retrieve the stored referer URL from the session
            referer_url = request.session.get('login_referer', None)
            if referer_url:
                return redirect(referer_url)
            else:
                return redirect('home')
        else:
            return render(request, 'autenticacao/login.html', {
                'mensagem': 'Credenciais inválidas'
            })

    return render(request, 'autenticacao/login.html')


def redirect_user_to_app(user):
    if user.groups.filter(name='editores de bandas').exists():
        return redirect('bands:user')
    elif user.groups.filter(name='editores de artigos').exists():
        return redirect('artigos:user_view')
    elif user.groups.filter(name='editores de curso').exists():
        return redirect('curso:user')
    else:
        return redirect('home')


def logout_view(request):

    referer_url = request.META.get('HTTP_REFERER')

    logout(request)
    return redirect(referer_url)