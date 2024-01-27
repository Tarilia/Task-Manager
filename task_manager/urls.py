from django.contrib import admin
from django.urls import path, include
from task_manager.views import IndexPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('users/', include('task_manager.users.urls')),
]
