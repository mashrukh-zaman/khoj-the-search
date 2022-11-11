from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
# from .models import Value

def index(request):
    # if request.method == 'POST':
        # form = khojForm(request.POST)
        
    input_value = request.POST.get('input_value')
    search_value = request.POST.get('search_value')
    print('++++++++++++++++++++++')
    print(type(input_value))
    # return HttpResponse(input_value)
    return render(request, 'user/index.html', {'title':'index'})
    # else:
    #     return HttpResponse('hello')

########### register here #####################################
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system ####################################
			htmly = get_template('user/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			##################################################################
			messages.success(request, f'Your account has been created! You are now able to log in.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'register here'})

################ login forms###################################################
def Login(request):
	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'Account does not exist. Please sign in')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})

# def khoj_view(request):
#     if request.method == 'POST':
#         form = khojForm(request.POST)
        
#         input_value = request.POST('input_value')
#         search_value = request.POST('search_value')
#         print('++++++++++++++++++++++')
#         print(input_value)
#         return HttpResponse(input_value)
    # if request.method == 'POST':
    #     input_value = request.POST.get['input_value']
    #     search_value = request.POST.get['search_value']
    #     form = khojForm(request.POST)
    #     if form.is_valid():
    #         pass  # does nothing, just trigger the validation
    # else:
    #     form = khojForm()
    # return render(request, 'index.html', {'form': form})
    # form = khojForm()
    # return render(request, 'user/khoj.html', {'form':form, 'title':'khoj'})

