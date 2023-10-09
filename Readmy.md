# Сборка проекта в docker compose

## Содержание
- [Настройка среды](#настройка_среды)
- [Сборка проекта](#сборка_проекта)

## Настройка среды
На машине для сборки должен быть установлен [Docker](https://www.docker.com/)

Создайте в корне проекта папку key и положите в неё файл ключа подписи.

В корне проекта создайте файл gradle.properties, выставьте настройки ключа:
```
android.enableJetifier=true
android.useAndroidX=true
org.gradle.jvmargs=-Xmx4096M

RELEASE_KEY_FILE=../key/<имя файла ключа>
RELEASE_STORE_PASSWORD=<пароль файла>
RELEASE_KEY_ALIAS=<имя ключа>
RELEASE_KEY_PASSWORD=<пароль ключа>
```
Если вы разработчик и вам не нужно собирать версию release, оставьте текст без изменений.

## Сборка проекта

Откройте терминал в корне проекта и введите команду:
```sh
$ docker-compose up --build
```
После выполнения сборки в корне проекта появится папка outputs с собранными apk и bundle версий release и debug.

