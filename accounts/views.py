from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from contacts.models import Contact
# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')
    elif request.method == 'POST':
        # Get form values
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "The username is taken.")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already reigistered.")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')


def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid Credentials.')
        print('post')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
    return redirect(request, 'index')


def dashboard(request):
    user_contacts = Contact.objects.filter(
        user_id=request.user.id).order_by('-contact_date')

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)
