from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .form import AddAnonMessageForm
from .models import AnonMessage

def home(request):
    return render(request, 'core/home.html')

def add_anon_message(request, pk):
    get_user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddAnonMessageForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = get_user
            var.save()
            messages.info(request, f'Secret message has been sent to {get_user.first_name}')
            return redirect('home')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('add-anon-message')
    else:
        get_user = User.objects.get(pk=pk)
        form = AddAnonMessageForm()
        context = {'form':form, 'get_user':get_user}
        return render(request, 'core/add_anon_message.html', context)
    
def all_anon_messages(request):
    obj = AnonMessage.objects.filter(user=request.user)
    context = {'obj':obj}
    return render(request, 'core/all_anon_messages.html', context)