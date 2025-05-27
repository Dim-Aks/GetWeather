import pytest
from ..models import CitySearch


# тест создания объекта CitySearch
@pytest.mark.django_db
def test_city_search_create():

    city = CitySearch.objects.create(
        city_name="Moscow",
        search_count=10
    )

    assert city.city_name == "Moscow"
    assert city.search_count == 10
    assert str(city) == "Moscow: 10"