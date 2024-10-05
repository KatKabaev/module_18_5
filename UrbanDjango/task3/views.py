from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def platform(request):
    return render(request, 'third_task/platform.html')

def game(request):
    context = {
        'one': 'Atomic Heart',
        'two': 'Cyberpunk 2077',
        'three': 'PayDay 2'
    }
    return render(request, 'third_task/games.html', context)

def cart(request):
    return render(request, 'third_task/cart.html')
