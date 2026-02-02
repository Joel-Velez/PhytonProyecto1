from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'mensaje' : 'Te Amo con toda el Alma'}
    return render(request, 'Miapp/index.html', context)
