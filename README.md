![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.001.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.003.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.004.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.005.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.006.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.007.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.008.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.009.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.010.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.011.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.012.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.013.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.014.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.013.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.015.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.016.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.017.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.018.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.019.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.020.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.021.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.022.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.023.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.024.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.025.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.026.jpg)
![site_schema_metapoet](https://raw.githubusercontent.com/tahoeivanova/diploma/master/Diploma_metapoet_presentation%20img.027.jpg)






# Poetry

Веб-сайт “MetaPoet”

Основная тема: применение инструментов backend-разработки для освещения творчества поэта в сети Интернет.

Стек технологий:
- Язык программирования Python
- Фреймворк Django
- СУБД Postgresql
- модуль озвучивания текста gtts
- модуль морфологического анализа текста Pymorphy2
- модуль API Django REST framework
- Frontend - визуальное оформление: CSS-стили, html-страницы, js-скрипты. Реализована кнопка переключения цветовых тем (светлый/темный режим). На главной странице использован js-скрипт архимедовой спирали.

Карта сайта: 
- - Главная страница - "home" - название сайта, имя автора стихов
- - - Стихи - все стихотворения
- - - - Словарь - разбивка слов стиха по частям речи
- - - - - Один стих - анимация набора текста
- - - - Аудио - генерация аудио стиха
- - - - Изменить - изменить стих  (для admin)
- - - - Удалить - удалить стих (для admin)
- - - Содержание - поиск по названию или по первой строке;
- - - Аналитика - сервис, подсчитывающий кол-во слов всего, кол-во уникальных слов, топ-100 слов, топ-100 по частям речи - через форму checkbox (сущ, прил, глагол)
- - API - "API" - скачать все стихи автора, все теги
- - TOKEN - генерация токена для API, обновление токена (для зарегистрированного пользователя)
- - ADD - добавить стихотворение (для admin)
- - Auth - войти.
- - Register - зарегистрироваться.
- - Exit - выйти.

Схема сайта:


![site_schema_metapoet](https://github.com/tahoeivanova/diploma/blob/master/Screen%20Shot%202020-06-04%20at%2017.17.01.png?raw=true)


Размещение проекта в сети Интернет:

- Web https://tranquil-refuge-12390.herokuapp.com/
- Docker-образ https://hub.docker.com/repository/docker/tahoeivanova/metapoet
- Docker-compose https://github.com/tahoeivanova/Poetry/blob/master/poetry/docker-compose.yml
- Git https://github.com/tahoeivanova/Poetry
