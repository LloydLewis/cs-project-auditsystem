from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

from audit_system import settings



def login_user(request): # View to login the user
    
    if request.method == 'POST':
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) #Checks if credentials match

        if user:
            # Redirects user to the home page
            login(request, user)
            return redirect('home')
        else:
            #returns a message if credentials dont match and sends back to login page

            messages.success(request, ('There was an error logging in. Try again'))
            return redirect('login')
    else:
        return render(request, 'login_system/login.html')


def logout_user(request):
    logout(request) #View to logout the user
    messages.success(request, ('You were logged out'))
    return redirect('login')
    


    



