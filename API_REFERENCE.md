# Описание Rest API
## _Хакатон Анапа 2022_

## Available methods (Доступные методы)

Для JWT аунтефикации используется библиотека djoser, все доступные методы и их описание можно посмотреть [здесь](https://djoser.readthedocs.io/en/latest/getting_started.html).

| Request type | Uri | Description |
| ------ | ------ | ------ |
| **GET** | /api/v1/auth/users/ | Получить список всех юзеров |
| **POST** | /api/v1/auth/users/ | Зарегистрироваться |
| **POST** | /api/v1/auth/jwt/create/ | Создать JWT токен |
| **POST** | /api/v1/auth/jwt/refresh/ | Обновить JWT токен |
| **GET** | /api/v1/map/markers/ | Получить список всех маркеров |
| **POST** | /api/v1/map/markers/upload/ | Загрузить новый маркер |


## Map. Upload marker
### **POST** "/map/markers/upload/" _form-data_
## Marker
| Name | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| image | string | **Yes** | Фотография объекта |
| marker_type | int | **Yes** | Тип оъекта: 1) Повреждения дороги. 2) Повреждения знака. 3) Проблемы с разметкой |
| gps | string | **Yes** | Ширина и долгота, разделенные запятой |
| address | string | No | Местонахождение по GPS |


## Map. Get all markers
### **GET** /map/markers/
| Name | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| List | list<Marker> | **Yes** | Список всех меток |