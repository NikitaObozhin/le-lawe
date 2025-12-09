#!/bin/bash
# Скрипт для настройки проекта на хостинге Reg.ru

echo "Настройка проекта на хостинге..."

# Активация виртуального окружения
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Сбор статических файлов
python manage.py collectstatic --noinput

# Применение миграций
python manage.py migrate

echo "Настройка завершена!"
echo "Не забудьте создать файл .env с переменными окружения"


