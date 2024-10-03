# views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to a login page or wherever you want
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
