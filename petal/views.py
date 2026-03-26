from django.shortcuts import render, redirect
from .models import PetalMessage

def home(request):
    if request.method == "POST":
        # Get data from the HTML form fields
        who = request.POST.get('for_whom')
        msg = request.POST.get('message')

        # Save it to the database
        PetalMessage.objects.create(recipient=who, message=msg)
        return redirect('home') # Refresh the page after saving

    return render(request, 'index.html')