from django.shortcuts import render
def view_users(request):
    return render(request,"utilisateurs/utilisateurs.html")
# Create your views here.
