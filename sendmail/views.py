from django.shortcuts import render
from django.core import mail
from django.core.mail import BadHeaderError, send_mass_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect


def index(request):


  connection = mail.get_connection()

  post1 = mail.EmailMessage('Error dont access this mail for you', 'invalid mail', 'information@send_emai', ['kosaki.digmee@gmail.com'])
  post1.attach('sample.txt', 'contents', 'text/plain')

  post2 = mail.EmailMessage('Subject here', 'feel your soul!!', 'information@send_email', ['bebejuli7339@gmail.com'])
  post2.attach('sample.txt', 'contents', 'text/plain')
  connection.send_messages([post1, post2])

  connection.close()

  return HttpResponse('<h1>email send complete</h1>')

# Create your views here.
