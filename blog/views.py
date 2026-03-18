from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, Contact

# Create your views here.


def render_posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {'posts': posts})


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, '¡Mensaje enviado correctamente! Nos pondremos en contacto pronto.')
            return redirect('contact')
        else:
            messages.error(request, 'Por favor, completa todos los campos.')
    
    return render(request, 'contact.html')
