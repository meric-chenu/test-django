from django.http import HttpResponse
from django.shortcuts import render

def view_contact(request):
    return render(request,"contact/contact.html")
