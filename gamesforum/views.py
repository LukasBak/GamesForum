from django.shortcuts import render, redirect
from .models import Thread
from .forms import ThreadForm

# Create your views here.

def forum(request):
    threads = Thread.objects.all()
    context = {'forum': forums}
    return render(request, 'gamesforum/forum.html', context)
    
def thread(request, pk):
    thread = Thread.objects.get(id=pk)
    context = {'thread': thread}
    return render(request, 'gamesforum/thread.html', context)

def createThread(request):
    form = ThreadForm()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('forum')

    context = {'form' : form}
    return render(request, 'gamesforum/new_thread', context)
    

