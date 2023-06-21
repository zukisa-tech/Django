
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import index, education, experience, projects

urlpatterns = [
    path('', index, name='index'),
    path('education/', education, name='education'),
    path('experience/', experience, name='experience'),
    path('projects/', projects, name='projects'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
