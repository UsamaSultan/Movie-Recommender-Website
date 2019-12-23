from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from models import CustomUser




def custom_redirect(url_name, *args, **kwargs):
    from django.core.urlresolvers import reverse 
    import urllib
    url = reverse(url_name, args = args)
    params = urllib.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)



def signup(request):

    if request.method == "POST":
        
        
        
        if request.POST.get('submit') == 'sign_in':
            
            form = CustomUserCreationForm(request.POST)
            form2 = AuthenticationForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                    if user.is_active:
                        login(request, user)
                        return custom_redirect('home', status='sis')
            else:
                    messages.error(request,'Username or Password  incorrect')
                    return custom_redirect('home', status='kmo')
            
        elif request.POST.get('submit') == 'sign_up':
            
            
            form = CustomUserCreationForm(request.POST)
            form2 = AuthenticationForm(request.POST)
        
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return custom_redirect('home', status='sus')
            
            else:
                messages.error(request, form.errors)
                return custom_redirect('home', status='kmosu')
                
            
            
    
    
    
    
    
            
    else:
        form = CustomUserCreationForm()
        form2 = AuthenticationForm()
    return render(request, 'users/signup.html', {'form': form , 'form2':form2})


def ce(request, email):
    
    print email
    
    u = CustomUser.objects.get(username=request.user.username)

    u.email = email
    
    u.save()
    
    return HttpResponseRedirect('home')