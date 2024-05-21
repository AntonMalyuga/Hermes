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

Для удаления виртуального окружения
```
sudo rm -rf venv/
```

## Удалить кэш
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```
* Установить пакеты для работы с проектом

```commandline
pip install -r requirements.txt
```


## Установка браузеров для playwrite
```commandline
playwright install
```




## Установка переменного окружения

В корневом каталоге необходимо открыть (создать) файл .env и записать туда логин и пароль от Гермес

ВАЖНО!
Убедиться, что в gitignore указано исключение файла .env (добавлена строка с надписьмю .env), иначе УД попадёт в GitHub.
