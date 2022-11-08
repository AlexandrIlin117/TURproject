
REST API ИТОГОВОЕ ЗАДАНИЕ (HW-04) Спринт 2 + 3
==============================================

*   [Interactive version made in the Postman application](https://documenter.getpostman.com/view/24238320/2s8YYPJ1aK#intro)
*   Требования к работе:
*   реализовать бизнес приложение с требуемым REST API
*   развернуть его на реальном сервере используя VPS
*   создать документацию к продукту описывающую REST API
Список зависимостей:



GET

[Получение всех данных из базы данных:](https://documenter.getpostman.com/view/24238320/2s8YYPJ1aK#95733cc7-85f7-4eda-9b5a-ea95758471d4 "Получение всех данных из базы данных:")

POST

[Создание новой записи о локации](https://documenter.getpostman.com/view/24238320/2s8YYPJ1aK#302a04ba-5d42-4bca-b4a5-2f25cb379af3 "Создание новой записи о локации")

GET

[Получение информации о записи с определённым ID](https://documenter.getpostman.com/view/24238320/2s8YYPJ1aK#739f87d9-cabd-42ac-90a8-ffb9b63d5226 "Получение информации о записи с определённым ID")

PATCH

[Редактирование записи](https://documenter.getpostman.com/view/24238320/2s8YYPJ1aK#b2158a35-2951-4087-86df-671a0714d90b "Редактирование записи")

GET

[Получение всех записей пользователя по его почте.](https://documenter.getpostman.com/view/24238320/2s8YYPJ1aK#b5f6533e-fb2a-4182-9e9e-063a60fce68a "Получение всех записей пользователя по его почте.")

REST API ИТОГОВОЕ ЗАДАНИЕ (HW-04) Спринт 2 + 3

Skillfactory итоговое задание:

*   реализовать бизнес приложение с требуемым REST API
*   развернуть его на реальном сервере используя VPS
*   создать документацию к продукту описывающую REST API

GET

Получение всех данных из базы данных:

http://62.84.126.164:8000/submitData

На запрос будет выдан JSON со всеми записями имеющимися в базе данных.

  
  

Example Request

Получение всех данных из базы данных: - упешный запрос.

    curl --location --request GET 'http://62.84.126.164:8000/submitData' \
    --data-raw ''

Example Response

200 OK

Body

Header(10)

View More

    [
      {
        "beautyTitle": "пер.",
        "title": "Я и водапад",
        "other_titles": "Гравити Фолз",
        "connect": "Швейцарию и Францию",
        "add_time": "2022-11-07T22:08:07+03:00",
        "status": "Добавлено",
        "user": {
          "email": "an_glask@example.com",
          "fam": "Селестабэль",

POST

Создание новой записи о локации

http://62.84.126.164:8000/submitData/

Метод возвращает только что созданую запись.

BODYraw

View More

    {
            "beautyTitle": "Страна сказок",
            "title": "Я и водапад",
            "other_titles": "Гравити Фолз",
            "connect": "Швейцарию и Францию",
            "add_time": "2022-11-07T22:08:07+03:00",
            "status": "Добавлено",
            "user": {
                "email": "an_glask@example.com",
                "fam": "Селестабэль",
                "name": "БеТтабел",
    

  
  

Создание новой записи о локации - попытка создать запись с некорректно заполненными полями JSON.

Example Request

View More

    curl --location --request POST 'http://62.84.126.164:8000/submitData/' \
    --data-raw '{
            "beautyTitle": "Страна сказок",
            "title": "Я и водапад",
          
            "connect": "Швейцарию и Францию",
            "add_time": "2022-11-07T22:08:07+03:00",
            "status": "Добавлено",
           
            "coords": {
                "latitude": 77.384,
    

Example Response

400 Bad Request

Body

Header(10)

    {
      "other_titles": [
        "This field is required."
      ],
      "user": [
        "This field is required."
      ]
    }

GET

Получение информации о записи с определённым ID

http://62.84.126.164:8000/submitData/4/

Указывайте явно ID записи как в примере.

  
  

Получение информации о записи с определённым ID - успешный запрос

Example Request

    curl --location --request GET 'http://62.84.126.164:8000/submitData/4/'

Example Response

200 OK

Body

Header(10)

View More

    {
      "beautyTitle": "Страна сказок",
      "title": "Я и водапад",
      "other_titles": "Гравити Фолз",
      "connect": "Швейцарию и Францию",
      "add_time": "2022-11-07T22:08:07+03:00",
      "status": "Рассматривается",
      "user": {
        "email": "an_glask@example.com",
        "fam": "Селестабэль",
        "name": "эбатабел",

PATCH

Редактирование записи

http://62.84.126.164:8000/submitData/4/

Редактирование доступно для всех полей кроме личной информации до изменения записи в поле "status".

BODYraw

View More

    {
        "beautyTitle": "Страна сказок",
        "title": "Я и водапад",
        "other_titles": "Гравити Фолз",
        "connect": "Швейцарию и Францию",
        "add_time": "2022-11-07T22:08:07+03:00",
        "status": "Добавлено",
        "user": {
            "email": "an_glask@example.com",
            "fam": "Селестабэль",
            "name": "эбатабел",
    

  
  

Редактирование записи - изменения успешно применены

Example Request

View More

    curl --location --request PATCH 'http://62.84.126.164:8000/submitData/4/' \
    --data-raw '{
        "beautyTitle": "Страна сказок",
        "title": "Я и водапад",
        "other_titles": "Гравити Фолз",
        "connect": "Швейцарию и Францию",
        "add_time": "2022-11-07T22:08:07+03:00",
        "status": "Добавлено",
        "user": {
            "email": "an_glask@example.com",
            "fam": "Селестабэль",
    

Example Response

200 OK

Body

Header(10)

    {
      "state:": 1,
      "message": "Изменения успешно применены"
    }

GET

Получение всех записей пользователя по его почте.

http://62.84.126.164:8000/submitData/?an\_glask@example.com

Указывайте почту явно после знака "?".

PARAMS

an\_glask@example.com

  
  

Example Request

Получение всех записей пользователя по его почте - выведены только записи для пользователя <an\_glask@example.com>

    curl --location --request GET 'http://62.84.126.164:8000/submitData/?user_id__email=an_glask@example.com' \
    --data-raw ''

Example Response

200 OK

Body

Header(10)

View More

    [
      {
        "beautyTitle": "пер.",
        "title": "Я и водапад",
        "other_titles": "Гравити Фолз",
        "connect": "Швейцарию и Францию",
        "add_time": "2022-11-07T22:08:07+03:00",
        "status": "Добавлено",
        "user": {
          "email": "an_glask@example.com",
          "fam": "Селестабэль",
