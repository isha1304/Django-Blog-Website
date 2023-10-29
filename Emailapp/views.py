from django.shortcuts import render
from Blog.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

def feedback(request):
    sub = forms.Feedback()
    if request.method == 'POST':
        sub = forms.Feedback(request.POST)
        subject = 'Welcome to Rucler Technologies'
        message = 'Good Efforts and Hope you are enjoying your Work'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})
# Create your views here.
