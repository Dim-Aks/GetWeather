import pytest
from django.urls import reverse
from rest_framework import status

from ..models import CitySearch


@pytest.fixture
def url():
    return reverse('city-search-list')


# Создаем тестовые данные
@pytest.fixture
def cities():
    cities = [
        CitySearch.objects.create(city_name="Москва", search_count=10),
        CitySearch.objects.create(city_name="Казань", search_count=5),
        CitySearch.objects.create(city_name="Саратов", search_count=3),
    ]
    return cities


# тест GET запроса к CitySearchList API
@pytest.mark.django_db
def test_city_search_list_get(client, cities, url):

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 3


# тест, что POST запрос к CitySearchList не разрешен
@pytest.mark.django_db
def test_city_search_list_post_not_allowed(client, url):

    response = client.post(url, data={'city_name': 'Rome', 'search_count': 10})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED