# Описание скрипта _upload.py_
## _Хакатон Анапа 2022_

#### Инициализация
Сначала нужно инициализировать и обьявить класс ClientJWT с параметрами, пример:
``` python
client_jwt = ClientJWT(base_url, username, password)
```
base_url - это домен вместе с /api/v1 (без слеша на конце)
username и password логин и пароль от аккаунта, чтобы создать сессию/получить ключ

#### Залить одну единственную метку на сервер
``` python
client_jwt.upload_marker("/path/to/image", marker_type, gps, address)
```

- Удачное выполнение, код 202_ACCEPTED

| Name | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| image | string(абсолютный путь) | **Yes** | Фотография объекта |
| marker_type | int | **Yes** | Тип оъекта: 1) Повреждения дороги. 2) Повреждения знака. 3) Проблемы с разметкой |
| gps | string | **Yes** | Ширина и долгота, разделенные запятой |
| address | string | **Yes** | Местонахождение по GPS |

#### Залить архив с метками на сервер
``` python
client_jwt.upload_markers_by_archive("/path/to/archive.zip")
```

- Удачное выполнение, код 202_ACCEPTED

