from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

from django.contrib import messages  # Import the messages module
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

def usersignup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            # You can add more fields to save like email, first name, last name, etc.
            user.save()
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('user_login')
        else:
            messages.error(request, 'Error during registration. Please try again.')
    else:
        form = UserRegistrationForm()
    return render(request, "Evisa/usersignup.html", {'form': form})


def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home upon successful login
        else:
            # Handle invalid login credentials
            return render(request, "Evisa/userlogin.html", {'error_message': 'Invalid username or password'})
    else:
        return render(request, "Evisa/userlogin.html", {})

def home(request):
    return render(request, "Evisa/home.html", {})

def applyvisa(request):
    return render(request, "Evisa/applyvisa.html", {})

def contactus(request):
    return render(request, "Evisa/contactus.html", {})

def aboutus(request):
    return render(request, "Evisa/aboutus.html", {})

def visatypes(request):
    return render(request, "Evisa/visatypes.html", {})

def app(request):
    return render(request, "Evisa/Schedule.html", {})