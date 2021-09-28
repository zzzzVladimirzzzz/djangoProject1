import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.


def index(request):
    appid = 'a644163645c77ff5a486b4bdaeb815a6'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res.get('main'):
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],

            }
            all_cities.append(city_info)
        else:
            city_info = {
                'city': city.name,
            }

    context = {'all_info': all_cities, 'form':form}

    return render(request, 'weather/index.html', context)