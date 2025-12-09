# -*- coding: utf-8 -*-

import os, sys

# Добавляем путь к проекту
sys.path.insert(0, '/var/www/u3351782/data/www/le-lawe.ru')

# Добавляем путь к виртуальному окружению
sys.path.insert(1, '/var/www/u3351782/data/www/le-lawe.ru/venv/lib/python3.10/site-packages')

# Загружаем переменные окружения из .env
from dotenv import load_dotenv
load_dotenv('/var/www/u3351782/data/www/le-lawe.ru/.env')

# Устанавливаем модуль настроек Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'education_portal.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

