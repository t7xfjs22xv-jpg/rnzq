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

# New function to view the inbox
def inbox(request):
    # This grabs all messages and puts the newest ones at the top
    all_messages = PetalMessage.objects.all().order_by('-id')
    return render(request, 'petal/inbox.html', {'messages': all_messages})