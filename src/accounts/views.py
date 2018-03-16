from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_conf']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'User already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                login(request, user)
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords didn\'t match'})

    else:
        return render(request, 'accounts/signup.html')

def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return render(request, 'accounts/login.html', {'error': 'sucess'})
        else:
            return render(request, 'accounts/login.html', {'error': 'The user name and password didn\'t match'})
    else:
        return render(request, 'accounts/login.html')
