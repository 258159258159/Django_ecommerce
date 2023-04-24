from django.http import HttpResponse
from django.shortcuts import render
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
    context = {
        "title": "Página de Contato",
        "content": "Bem-vindo a Página de Contato"
    }
    return render(request, "contact/view.html", context)
