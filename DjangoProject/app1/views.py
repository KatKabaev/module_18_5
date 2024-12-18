from django.shortcuts import render


# Create your views here.
def platform(request):
    return render(request, 'first_task/platform.html')

def game(request):
    context = {'games': ['Atomic Heart', "Cyberpunk 2077", 'PayDay 2']}
    con = {'context': context['games']}
    return render(request, 'first_task/games.html', con)

def cart(request):
    return render(request, 'first_task/cart.html')
