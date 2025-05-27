import pytest
from django.urls import reverse

from ..forms import CityForm
from ..models import CitySearch

@pytest.fixture
def url():
    return reverse('index')


# тест get главной страницы
def test_index_view_get(client, url):

    response = client.get(url)

    assert response.status_code == 200
    assert 'weather/index.html' in [t.name for t in response.templates]
    assert isinstance(response.context['form'], CityForm)
    assert 'city' not in response.context['form'].initial


# тест get с городом в сессии
@pytest.mark.django_db
def test_index_view_get(client, url):

    # Устанавливаем город в сессию
    session = client.session
    session['last_searched_city'] = 'Moscow'
    session.save()

    response = client.get(url)

    assert response.status_code == 200
    assert response.context['form'].initial['city'] == 'Moscow'


# тест POST запроса с валидным городом
@pytest.mark.django_db
def test_index_view_post_valid(client, url):

    response = client.post(url, {'city': 'Moscow'})

    # Проверяем редирект или успешный рендеринг
    if response.status_code == 302:
        assert response.url == reverse('weather')
        assert 'T' not in response.context['weather'][0][0]  # Время должно быть обработано
    else:
        assert response.status_code == 200
        assert 'weather/weather.html' in [t.name for t in response.templates]
        assert response.context['city'] == 'Moscow'

    # Проверяем сессию
    session = client.session
    assert session['last_searched_city'] == 'Moscow'

    # Проверяем, что счетчик увеличился
    city_search = CitySearch.objects.get(city_name='Moscow')
    assert city_search.search_count == 1


# тест POST запроса с не валидным городом
@pytest.mark.django_db
def test_index_view_post_invalid(client, url):

    response = client.post(url, {'city': 'Abrakadabra'})

    assert response.status_code == 200
    assert 'weather/index.html' in [t.name for t in response.templates]
    assert 'error_message' in response.context
    assert response.context['error_message'] == 'Город не найден'
