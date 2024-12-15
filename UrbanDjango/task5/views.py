from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.
def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        users = ["Ekaterina", "Marina", "Mikhail"]
        info = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username not in users and password == repeat_password and age >= '18':
                users.append(username)
                print(f'Updated names: {users}')
                return HttpResponse(f'Приветствуем, {username}!')

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

            elif age < '18':
                info['error'] = 'Вы должны быть старше 18'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

            elif username in users:
                info['error'] = 'Пользователь уже существует'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

    else:
        form = UserRegister()
        info = {'form': form}
    return render(request, 'fifth_task/registration_page.html', context=info)

