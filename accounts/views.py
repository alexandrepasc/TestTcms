from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup(request):
    setattr(request, 'view', 'signup')

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})
