import pytest
from ..forms import CityForm


# тест формы
def test_city_form_valid():

    form_data = {'city': 'Москва'}
    form = CityForm(data=form_data)

    assert form.fields['city'].label == 'Город'
    assert form.is_valid() is True
    assert form.cleaned_data['city'] == 'Москва'
    assert form.errors == {}


# тест превышения максимальной длины
def test_city_form_max_length():

    city = 'А' * 51
    form = CityForm(data={'city': city})

    assert form.is_valid() is False
    assert 'city' in form.errors
    assert 'Убедитесь, что это значение содержит не более 50 символов' in form.errors['city'][0]