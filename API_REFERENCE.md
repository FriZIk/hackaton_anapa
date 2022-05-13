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
