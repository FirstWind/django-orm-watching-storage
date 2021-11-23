# Пульт охраны банка

Программа для фиксирования посещений хранилища сотрудниками банка в базе данных.

### Как установить

Python3 должен быть уже установлен. 

- Скачайте код с GitHab 
```
git clone https://github.com/FirstWind/django-orm-watching-storage.git
```
- Установите виртуальное окружение
- используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
- Запустите сайт командой 
```python
python main.py
```
- Перейдите на сайт по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Подключение к Базе Данных
Измените значения в файле `project/settings.py` на:  
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": "checkpoint.devman.org",
        "PORT": "5434",
        "NAME": "checkpoint",
        "USER": "guard",
        "PASSWORD": "osim5",
    }
}

SECRET_KEY = "REPLACE_ME"
```
В параметре `TIME_ZONE` установите временную зону вашего региона

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).