### Hexlet tests and linter status:
[![Actions Status](https://github.com/Tarilia/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Tarilia/python-project-52/actions)
[![Linter](https://github.com/Tarilia/python-project-52/actions/workflows/test.yml/badge.svg)](https://github.com/Tarilia/python-project-52/actions/workflows/test.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/1a522ed94badc1ed0777/maintainability)](https://codeclimate.com/github/Tarilia/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1a522ed94badc1ed0777/test_coverage)](https://codeclimate.com/github/Tarilia/python-project-52/test_coverage)

### [Task Manager](https://task-manager-bkxd.onrender.com)

 - веб-приложение, созданное на основе фреймворка Django.
 - для верстки используется Bootstrap5.
 - позволяет пользователям создавать задачи, назначать исполнителей и отслеживать статусы задач.

### Установка:

 - клонировать этот репозиторий
 - poetry install
 - make migrate
 - make dev - для локального использования
 - make start - для продакшена

 Для настройки приложения, нужно установить в .env следующие переменные среды:

 - DEBUG
 - DATABASE_URL
 - SECRET_KEY
 - ROLLBAR


### Визуализация:

 - главная страница:

[![image.png](https://i.postimg.cc/TwXhhrsj/image.png)](https://postimg.cc/2q2CKBr3)

 - для доступа к основному функционалу приложения, необходима аутентификация и авторизация пользователя:

[![image.png](https://i.postimg.cc/TYP1y2ts/image.png)](https://postimg.cc/Jt9Mv8V3)

[![image.png](https://i.postimg.cc/wBN76WwT/image.png)](https://postimg.cc/NyggDxhW)

 - можно проссматривать все созданные задачи/статусы/метки. Всех зарегистрированных пользователей. Для задач доступна фильтрация:

[![image.png](https://i.postimg.cc/c45HfqjL/image.png)](https://postimg.cc/KRBxyWx6)

[![image.png](https://i.postimg.cc/NFsMkQB5/image.png)](https://postimg.cc/phSR2b9H)

 - пользователей/задачи/статусы/метки можно создавать, редактировать и удалять:

[![image.png](https://i.postimg.cc/yxLNf28n/image.png)](https://postimg.cc/n9QZrR7Q)

[![image.png](https://i.postimg.cc/tTtJ6s0K/image.png)](https://postimg.cc/HcnTDskz)

[![image.png](https://i.postimg.cc/3r1WJ0Fp/image.png)](https://postimg.cc/dD7J51Xt)

 - информацию по задаче можно проссмотреть:

[![image.png](https://i.postimg.cc/SK9kPTzj/image.png)](https://postimg.cc/qtpPhGwd)
