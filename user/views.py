from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import *
import re

def index(request):
	# if request.method == 'POST':
	try:
		input_value = request.POST['input_value']
		search_value = request.POST['search_value']

		# is_existing_value = Value.objects.all().exists()
		# if is_existing_value:
		# 	Value.objects.update(input_value = input_value, search_value = search_value, user_id = request.user.id)

		# else:
		# 	input_db = Value(input_value=input_value, search_value=search_value, user_id=request.user.id)
		# 	input_db.save()
		input_db = Value(input_value=input_value, search_value=search_value, user_id=request.user.id)
		input_db.save()
		test = Value.objects.filter().order_by('-created_at')[0].input_value
		print('test:', test)
		# numbers = Value.objects.filter().values().first()['input_value']
		# numbers = Value.objects.filter().order_by('-data')[0]
		numbers = Value.objects.filter().order_by('-created_at')[0].input_value
		numbers = re.findall(r'\d+', numbers)
		print(numbers)
		if (search_value in numbers):
			print('True')
			messages.success(request, f'found')
		else:
			print('False')
			messages.info(request, f'not found')
		print(Value.objects.all())
		print(Value.objects.filter().values().first()['user_id'])
		print(request.user.id)

		return render(request, 'user/index.html', {'title':'index'})
	except:
		return render(request, 'user/index.html', {'title':'index'})
	# else:
	# 	return HttpResponse('We are currently working on this page. Please visit later')

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


from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def api_view(request):
	if request.method == 'GET':
		user_id = request.user.id
		start_datetime = Value.objects.filter().order_by('-created_at')[0].created_at
		start_input_value = Value.objects.filter().order_by('-created_at')[0].input_value
		end_datetime = Value.objects.filter().order_by('created_at')[0].created_at
		end_input_value = Value.objects.filter().order_by('created_at')[0].input_value

		return JsonResponse(
                    {
						"status": "success",
						"user_id": user_id, 
						"payload": {
							"timestamp": start_datetime, 
							"input_value": start_input_value,
							"timestamp1": end_datetime,
							"input_value1": end_input_value,
						},
					},			
                    
                    	status=status.HTTP_200_OK, 
                )

