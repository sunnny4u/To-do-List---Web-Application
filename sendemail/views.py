from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings


def emailView(request):
    if request.method == 'POST':
    	name = request.POST['firstname']
    	message = request.POST['subject']
    	mail = request.POST['mail']

    	send_mail(mail,message,settings.EMAIL_HOST_USER,['example@example.com'],fail_silently=False)
    return render(request, "contact.html")

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
