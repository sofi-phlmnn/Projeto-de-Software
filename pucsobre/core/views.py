from django.shortcuts import render

def sobre_equipe(request):
    return render(request, 'sobre.html')