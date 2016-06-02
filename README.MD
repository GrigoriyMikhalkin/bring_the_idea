# Bring The Idea

Приложение для шэринга идей, позволяющее рейтить идеи и находить потенциальных партнеров.

## Перед установкой

Далее рассматривается установка проекта в ОС Ubuntu версии > 14.04. Но, в принципе, должно работать и на более старых версиях. А так же на других Linux дистрибутивах, где доступны нижеупомянутые технологии.

Технологии которые должны быть установлены перед установкой проекта:

1. Python 3.4
2. pip3
3. Git
4. PostgreSQL

## Установка

Первым делом нужно установить виртуальную среду для проекта. Переходим в директорию, где собираемся устанавливать проект, далее выполняем команды:

    pip3 install virtualenv
    mkdir bring_the_idea
    cd bring_the_idea
    virtualenv -p /usr/bin/python3.4 venv
    source venv/bin/activate

В установленную директорию клонируем проект:

    git clone https://github.com/GrigoriyMikhalkin/bring_the_idea.git
    cd bring_the_idea

Устанавливаем зависимости:

    pip install -r requirements.txt

Следующий этап -- настройка базы данных. Перед тем как выполнять нижеприведенные команды, необходимо установить PostgreSQL(инструкция для Ubuntu: https://help.ubuntu.com/community/PostgreSQL ).

Создадим базу данных и пользователя:

    sudo su postgres
    createdb btidb
    createuser -P

Дадим доступ к нашей базе данных, только что созданному пользователю:

       psql
       GRANT ALL PRIVELEGES ON DATABASE btidb TO имя_пользователя

Теперь нужно прописать имя пользователя и пароль в настройках. В файле bring_the_idea/private_settings.py, в словаре DATABASES.default, вместо '' вставляем:

    'USER': "имя пользователя",
    'PASSWORD': "пароль",

Наконец, применяем миграции:

    python manage.py migrate

## Запуск проекта

** Необязательно ** Из корневой директории проекта запускаем Tornado сервер:
    python run_websock.py

Запускаем Django сервер:

    python manage.py runserver

В браузере заходим на http://localhost:8000