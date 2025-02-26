# Пульт охраны банка

Пульт охраны - этой сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников.

### Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```pip install -r requirements.txt```
### Как настроить

Для работы сайту необходим файл .env с переменными окружения:

`DB_ENGINE` - указание СУБД для работы с базой данных

`DB_HOST` - адрес хоста вашего сервера базы данных

`DB_PORT` - порт подключения

`DB_NAME` - название базы данных

`DB_USER` - имя пользователя БД

`DB_PASSWORD` - пароль пользователя БД

`DEBUG` - Режим отладки. Если установлен в `True`, сайт запускается в соответствующем режиме.
### Как использовать

Для запуска сервера с сайтом запустите скрипт `manager.py`:

```shell
user@user: ~/$: python manage.py runserver 0.0.0.0:8000
```
*Порт 8000 указан по умолчанию -- при желании, установите тот, который будет вам удобен*