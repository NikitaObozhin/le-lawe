from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core.cache import cache
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

def index(request):
    context = {
        'title': 'Главная страница - Образовательный портал | Новости, задания и курсы',
        'description': 'Добро пожаловать на образовательный портал! Актуальные новости в сфере образования, банк заданий с решениями, образовательные курсы, библиотека учебных материалов и дополнительные ресурсы для студентов.',
        'keywords': 'образование, обучение, новости, задания, задачи, учебные материалы',
    }
    return render(request, 'portal/index.html', context)

def news(request):
    context = {
        'title': 'Новости образования - Образовательный портал | Актуальные события и обновления',
        'description': 'Читайте актуальные новости образовательного портала: обновления платформы, новые задания и курсы, веб-семинары, события в сфере образования. Будьте в курсе всех изменений и новинок.',
        'keywords': 'новости, образование, события, обновления',
    }
    return render(request, 'portal/news.html', context)

def news_detail(request, news_id):
    news_titles = {
        1: 'Новое обновление портала - Образовательный портал',
        2: 'Добавлены новые задания в банк задач - Образовательный портал',
        3: 'Открыт новый курс "Основы программирования" - Образовательный портал',
    }
    news_descriptions = {
        1: 'Узнайте о новом обновлении образовательного портала: улучшенный интерфейс, новые функции для работы с заданиями, оптимизация для мобильных устройств и улучшенная навигация.',
        2: 'В банк заданий добавлено более 50 новых задач по математике, программированию, физике и гуманитарным наукам. Все задания имеют различные уровни сложности и подробные решения.',
        3: 'Приглашаем на новый образовательный курс "Основы программирования". Курс включает теоретические материалы, практические задания и тесты для самопроверки.',
    }
    context = {
        'title': news_titles.get(news_id, f'Новость {news_id} - Образовательный портал'),
        'description': news_descriptions.get(news_id, f'Подробная информация о новости {news_id} образовательного портала'),
        'keywords': 'новости, образование, события',
        'news_id': news_id,
    }
    return render(request, 'portal/news_detail.html', context)

def tasks(request):
    context = {
        'title': 'Банк заданий - Образовательный портал | Задачи по математике, программированию и физике',
        'description': 'Большая коллекция учебных заданий и задач для студентов: математика (производные, интегралы), программирование (массивы, алгоритмы), физика (механика, термодинамика). Все задания с решениями и разными уровнями сложности.',
        'keywords': 'задания, задачи, упражнения, обучение, практика',
    }
    return render(request, 'portal/tasks.html', context)

def task_detail(request, task_id):
    task_titles = {
        1: 'Задание: Производные функций - Образовательный портал | Решение задач с примерами',
        2: 'Задание: Интегралы - Образовательный портал | Вычисление определенных и неопределенных интегралов',
        3: 'Задание: Массивы и циклы - Образовательный портал | Основы программирования',
    }
    task_descriptions = {
        1: 'Задачи на нахождение производных различных функций. Включает 10 задач с подробными решениями. Уровень сложности: средний. Категория: математика.',
        2: 'Задачи на вычисление определенных и неопределенных интегралов с подробными решениями и пошаговыми объяснениями. Уровень сложности: продвинутый.',
        3: 'Основы работы с массивами и циклами в программировании. Практические примеры на Python. Уровень сложности: начальный. Категория: программирование.',
    }
    context = {
        'title': task_titles.get(task_id, f'Задание {task_id} - Образовательный портал'),
        'description': task_descriptions.get(task_id, f'Подробное описание задания {task_id} с условиями задач и решениями'),
        'keywords': 'задания, задачи, упражнения, обучение',
        'task_id': task_id,
    }
    return render(request, 'portal/task_detail.html', context)

def about(request):
    context = {
        'title': 'О портале - Образовательный портал | Миссия, возможности и история',
        'description': 'Узнайте больше об образовательном портале: наша миссия, возможности платформы, история создания, команда разработчиков. Бесплатный доступ ко всем материалам, регулярные обновления контента, удобный интерфейс.',
        'keywords': 'о портале, информация, образование',
    }
    return render(request, 'portal/about.html', context)

def contacts(request):
    context = {
        'title': 'Контакты - Образовательный портал | Свяжитесь с нами',
        'description': 'Контактная информация образовательного портала: электронная почта для общих вопросов и технической поддержки, телефон горячей линии, адрес офиса. Мы отвечаем на все обращения в течение 24 часов.',
        'keywords': 'контакты, связь, обратная связь',
    }
    return render(request, 'portal/contacts.html', context)

def resources(request):
    context = {
        'title': 'Дополнительные ресурсы - Образовательный портал | Видеоуроки, инструменты и ссылки',
        'description': 'Дополнительные образовательные ресурсы для углубленного изучения: видеоуроки, интерактивные задания, веб-семинары, онлайн-калькуляторы, графические редакторы, компиляторы и полезные ссылки.',
        'keywords': 'ресурсы, материалы, обучение, образование',
    }
    return render(request, 'portal/resources.html', context)

def courses(request):
    context = {
        'title': 'Образовательные курсы - Образовательный портал | Программирование, математика, физика',
        'description': 'Образовательные курсы и программы для самостоятельного изучения: программирование (основы, веб-разработка), математика (математический анализ, линейная алгебра), физика (механика, электромагнетизм). Все курсы бесплатны и включают теорию, практику и тесты.',
        'keywords': 'курсы, программы, обучение, образование',
    }
    return render(request, 'portal/courses.html', context)

def library(request):
    context = {
        'title': 'Библиотека учебных материалов - Образовательный портал | Учебники, справочники, статьи',
        'description': 'Библиотека учебных материалов, книг и пособий: учебники по математике, программированию и физике, справочники формул, научные статьи и публикации. Более 200 учебных пособий доступны онлайн.',
        'keywords': 'библиотека, книги, материалы, обучение',
    }
    return render(request, 'portal/library.html', context)

def faq(request):
    context = {
        'title': 'FAQ - Часто задаваемые вопросы - Образовательный портал | Помощь и ответы',
        'description': 'Ответы на часто задаваемые вопросы об образовательном портале: регистрация, стоимость использования, обновление контента, работа с заданиями, технические вопросы, мобильная версия, защита контента.',
        'keywords': 'FAQ, вопросы, ответы, помощь',
    }
    return render(request, 'portal/faq.html', context)

def custom_404(request, exception=None):
    """Обработчик ошибки 404"""
    from django.template import loader
    from django.http import HttpResponseNotFound
    context = {
        'title': '404 - Страница не найдена',
        'description': 'Страница не найдена - Образовательный портал',
        'keywords': '404, ошибка, страница не найдена',
    }
    template = loader.get_template('404.html')
    return HttpResponseNotFound(template.render(context, request))

def custom_500(request):
    """Обработчик ошибки 500"""
    from django.template import loader
    from django.http import HttpResponseServerError
    context = {
        'title': '500 - Ошибка сервера',
        'description': 'Внутренняя ошибка сервера - Образовательный портал',
        'keywords': '500, ошибка сервера',
    }
    template = loader.get_template('500.html')
    return HttpResponseServerError(template.render(context, request))

def custom_403(request, exception=None):
    """Обработчик ошибки 403"""
    from django.template import loader
    from django.http import HttpResponseForbidden
    context = {
        'title': '403 - Доступ запрещен',
        'description': 'Доступ запрещен - Образовательный портал',
        'keywords': '403, доступ запрещен, ошибка доступа',
    }
    template = loader.get_template('403.html')
    return HttpResponseForbidden(template.render(context, request))

def custom_400(request, exception=None):
    """Обработчик ошибки 400"""
    from django.template import loader
    from django.http import HttpResponseBadRequest
    context = {
        'title': '400 - Неверный запрос',
        'description': 'Неверный запрос - Образовательный портал',
        'keywords': '400, неверный запрос, ошибка запроса',
    }
    template = loader.get_template('400.html')
    return HttpResponseBadRequest(template.render(context, request))

@require_http_methods(["POST"])
def update_user_activity(request):
    """Обновляет активность пользователя и возвращает количество активных пользователей"""
    # Получаем уникальный идентификатор сессии
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    current_time = timezone.now().timestamp()
    active_users_key = 'active_users_list'
    
    # Получаем список активных пользователей из кэша
    active_users = cache.get(active_users_key, {})
    
    # Обновляем время активности текущего пользователя
    active_users[session_key] = current_time
    
    # Удаляем неактивных пользователей (неактивны более 30 секунд)
    active_users = {k: v for k, v in active_users.items() 
                   if current_time - v < 30}
    
    # Сохраняем обновленный список в кэш на 2 минуты
    cache.set(active_users_key, active_users, 120)
    active_count = len(active_users)
    
    return JsonResponse({'count': active_count})

def get_active_users_count(request):
    """Возвращает количество активных пользователей"""
    active_users_key = 'active_users_list'
    active_users = cache.get(active_users_key, {})
    current_time = timezone.now().timestamp()
    
    # Удаляем неактивных пользователей (неактивны более 30 секунд)
    active_users = {k: v for k, v in active_users.items() 
                   if current_time - v < 30}
    
    # Сохраняем очищенный список
    cache.set(active_users_key, active_users, 120)
    return JsonResponse({'count': len(active_users)})

