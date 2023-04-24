from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    context = {
        "title": "Página Principal",
        "content": "Bem-vindo a Página Principal"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Página Sobre",
        "content": "Bem-vindo a Página Sobre"
    }
    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página de Contato",
        "content": "Bem-vindo a Página de Contato",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        #if request.method == "POST":
        #print(request.POST)
        #print(request.POST.get('nome_completo'))
        #print(request.POST.get('email'))
        #print(request.POST.get('mensagem'))
    return render(request, "contact/view.html", context)
