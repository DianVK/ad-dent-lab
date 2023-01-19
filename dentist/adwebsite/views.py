from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request,'home.html', {})

def courier(request):
	return render(request,'courier.html', {})

def aligners(request):
	return render(request,'aligners.html', {})

def about(request):
	return render(request,'about.html', {})

def products(request):
	return render(request,'products.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		new_name = str(message_name + " - " + message_email)
		new_message = str(message + " - " + message_email)
		# send an email
		send_mail(
			new_name, # subject
			new_message, # message
			message_email, # from email
			['addentlab23@gmail.com'], # To Email
			)

		return render(request, 'contact.html', {'message_name': message_name},)

	else:
		return render(request, 'contact.html', {})