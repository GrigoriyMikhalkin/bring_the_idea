# Bring The Idea

Приложение для шэринга идей, позволяющее рейтить идеи и находить потенциальных партнеров.

## Перед установкой

Далее рассматривается установка проекта в ОС Ubuntu версии > 14.04. Но, в принципе, должно работать и на более старых версиях. А так же на других Linux дистрибутивах, где доступны нижеупомянутые технологии.

Технологии которые должны быть установлены перед установкой проекта:

1. Git(https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. Docker(https://docs.docker.com/engine/installation/)
3. Docker-Compose(https://docs.docker.com/compose/install/), должна быть установлена версия >= 1.7

## Установка

Клонируем репозиторий и заходим в коренную директорию проекта:

    git clone https://github.com/GrigoriyMikhalkin/bring_the_idea.git
    cd bring_the_idea

Устанавливаем образ определенный в Dockerfile проекта:

    docker-compose build

Если данная команда кидает ошибку о том, что docker сервер не обнаружен, запускаем ее с `sudo`.

После того как образ был установлен, запускаем контейнер:

    docker-compose up -d

Применяем миграции к базе данных:

    sudo docker exec web python3 /code/manage.py migrate

Перезапускаем контейнер с Django приложением:

    sudo docker restart web

Готово. В браузере заходим на http://localhost:8000
