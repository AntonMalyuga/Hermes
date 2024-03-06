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
python .\venv\Scripts\activate
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

* Установить в переменное окружение логин и пароль пользователя для запуска тестов
```commandline
#### Для линукс
export LOGIN=Логин
export PASSWORD=Пароль
#### Для виндоус
export LOGIN=Логин
export PASSWORD=Пароль
```

## Установка драйверов браузера

Для работы веб драйвера в системе Linux необходимо добавить сам драйвер браузера из GitHub 
* Firefox https://github.com/mozilla/geckodriver/releases/
* Chrome

Скачиваем необходимый файл (указан пример):
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux32.tar.gz
```

Вытаскиваем файл из архива (указан пример):
```
tar -xvzf geckodriver*
```

Даем нужные права драйверу (указан пример):
```
sudo chmod +x geckodriver
```

Отправляем драйвер в папку где его будет искать Selenium (указан пример т.к. везде разные пути):
```
sudo mv geckodriver /Документы
```


