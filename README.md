# GetWeather

Это веб-приложение, созданное на Django, которое позволяет пользователям искать информацию о погоде в конкретном городе с помощью API Open-Meteo (https://open-meteo.com/).

# Особенности

*   **Поиск города:** пользователи могут ввести название города и просмотреть текущий прогноз погоды.
*   **Отображение данных:** данные о погоде отображаются в удобночитаемом формате.
*   **API Django REST Framework:** предоставляется эндпоинт для получения информации о наиболее часто запрашиваемых городах.
*   **Docker:**  приложение контейнеризировано с помощью Docker для упрощения развертывания.
*   **Тестирование:**  модульные тесты написаны с помощью pytest и покрывают 96%.
*   **Последний найденный город:** запоминает последний найденный город с помощью сеансов и предлагает его в качестве выбора.

# Используемые технологии

*   **Django**
*   **Django REST Framework**
*   **Open-Meteo API**
*   **Requests**
*   **pytest**
*   **SQLite** (была выбрана для простоты и скорости разработки)
*   **Docker**

# ⚙️ Требования

asgiref==3.8.1
certifi==2025.4.26
charset-normalizer==3.4.2
colorama==0.4.6
coverage==7.8.2
Django==5.2.1
djangorestframework==3.16.0
idna==3.10
iniconfig==2.1.0
packaging==25.0
pluggy==1.6.0
pytest==8.3.5
pytest-cov==6.1.1
pytest-django==4.11.1
requests==2.32.3
sqlparse==0.5.3
tzdata==2025.2
urllib3==2.4.0

 # 🛠 Установка

* Клонировать репозиторий:

git clone https://github.com/Dim-Aks/GetWeather.git

cd getweather

cd get_weather

* Соберите и запустите контейнеры Docker:

docker-compose up --build

* Откройте веб-браузер и перейдите по адресу `http://localhost:8000`

* Эндпоинт `/api/city_searches/` возвращает список наиболее часто запрашиваемых городов

Можно запустить локально, тогда после того, как склонирован репозиторий и перешли в нужную дерикторию продолжайте далее выполнять шаги

* Создать виртуальное окружение:

python -m venv venv

source venv/bin/activate  - Linux/Mac

venv\Scripts\activate  - Windows

* Установить зависимости:

pip install -r requirements.txt

* Запуск сервера:

python manage.py runserver

# 🧪 Тестирование

Запуск тестов:

pytest --cov

# 📬 Контакты
**Дмитрий**

Email: kiton444@gmail.com

Telegram: @Dim_Ax
