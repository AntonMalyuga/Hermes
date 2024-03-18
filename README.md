# Hermes
Тестирование платформы Гермес

## Начало работы

* Установить модуль для виртуального окружения (если не установлен)

```commandline
 python -m venv venv
```

* Активировать виртуальное окружение

Для Windows
```commandline
venv\Scripts\activate
```

Для Linux

```commandline
source venv/bin/activate
```

Для деактивации виртуального окружения набрать команду

```commandline
deactivate
```

* Установить пакеты для работы с проектом

```commandline
pip install -r requirements.txt
```


## Установка браузера для linux

Для работы веб драйвера в системе Linux необходимо добавить сам драйвер браузера из GitHub
* Chrome https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

Скачиваем необходимый файл браузера (указан пример):
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

Устанавливаем браузер (указан пример):
```
dpkg -i google-chrome-stable_current_amd64.deb
```

## Установка переменного окружения

В корневом каталоге необходимо открыть (создать) файл .env и записать туда логин и пароль от Гермес

ВАЖНО!
Убедиться, что в gitignore указано исключение файла .env (добавлена строка с надписьмю .env), иначе УД попадёт в GitHub.
