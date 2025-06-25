from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Thanks for reaching out! I’ll get back to you soon.')
            return redirect('contact')
        
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})