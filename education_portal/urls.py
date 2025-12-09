"""
URL configuration for education_portal project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.http import HttpResponse, FileResponse
from pathlib import Path

def robots_txt(request):
    robots_path = settings.BASE_DIR / 'static' / 'robots.txt'
    if robots_path.exists():
        with open(robots_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return HttpResponse(content, content_type='text/plain')
    return HttpResponse('User-agent: *\nAllow: /', content_type='text/plain')

def sitemap_xml(request):
    sitemap_path = settings.BASE_DIR / 'static' / 'sitemap.xml'
    if sitemap_path.exists():
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return HttpResponse(content, content_type='application/xml')
    return HttpResponse('<?xml version="1.0" encoding="UTF-8"?><urlset></urlset>', content_type='application/xml')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls')),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap_xml),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Обработка ошибок
handler404 = 'portal.views.custom_404'
handler500 = 'portal.views.custom_500'
handler403 = 'portal.views.custom_403'
handler400 = 'portal.views.custom_400'

