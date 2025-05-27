import requests
from django.shortcuts import render
from rest_framework import generics

from .forms import CityForm
from .models import CitySearch
from .serializers import CitySearchSerializer


# получаем данные о погоде
def get_weather(city):

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    data = response.json()

    if not data or 'results' not in data or not data['results']:
        return None

    latitude = data['results'][0]['latitude'] # получаем широту
    longitude = data['results'][0]['longitude'] # получаем долготу

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    return weather_data


# главная страница с формой
def index(request):

    last_searched_city = request.session.get('last_searched_city') # получаем последний город из сессии

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather = get_weather(city)
            if weather:
                # сохраняем город в сессию
                request.session['last_searched_city'] = city
                # увеличиваем счетчик поиска города
                city_search, created = CitySearch.objects.get_or_create(city_name=city)
                city_search.search_count += 1
                city_search.save()

                # убираем из даты лишнее
                time_list = []
                for elem in weather['hourly']['time']:
                    time_list.append(elem.replace('T', ' '))
                weather['hourly']['time'] = time_list

                # подготоваливаем данные для шаблона
                data = zip(weather['hourly']['time'],
                                  weather['hourly']['temperature_2m'],
                                  weather['hourly']['relativehumidity_2m'],
                                  weather['hourly']['windspeed_10m'])
                context = {
                    'weather': data,
                    'city': city,
                }

                return render(request, 'weather/weather.html', context)
            else:
                return render(request, 'weather/index.html', {'form': form, 'error_message': 'Город не найден'})
    else:
        # если в сессии есть город, подставляем его
        form = CityForm(initial={'city': last_searched_city} if last_searched_city else None)
        return render(request, 'weather/index.html', {'form': form})


class CitySearchList(generics.ListAPIView):
    queryset = CitySearch.objects.all()
    serializer_class = CitySearchSerializer
