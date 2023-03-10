from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .form import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Employee
from .form import Forum


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })

            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                login(request, user)               
                return render(request,'login.html')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})




def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, 'homepage.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')    
    
@login_required


# Create your views here.
def index(request):
    emp=Employee.objects.all()
    context={
        'emp':emp
    }
    return render(request,'homepage.html',context)

def add(request):
    if request.method=="POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         address=request.POST.get('address')
         mobile=request.POST.get('mobile')
         

         emp=Employee(
            name = name,
         email = email,
         address = address,
         mobile = mobile
         )

         
         emp.save()
         return redirect('home')
    return render(request,'homepage.html')

def Edit(request):
    emp=Employee.objects.all()
    context={
        'emp':emp
    }
    return render(request,'homepage.html',context)

def Update(request,id):
    if request.method == "POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         address=request.POST.get('address')
         mobile=request.POST.get('mobile')
         

         emp=Employee(
            id=id,
        name = name,
        email = email,
        address = address,
        mobile = mobile
         )
         emp.save()
         return redirect('home')
    return render(request,'homepage.html')

def delete(request,id):
    emp=Employee.objects.filter(id=id)
    emp.delete()
    context={
        'emp':emp
    }
    return redirect('home')
