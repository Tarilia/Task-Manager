from django.contrib import admin
from django.urls import path, include
from task_manager.views import IndexPageView, LoginUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('login/', LoginUser.as_view(), name='login'),
    path('users/', include('task_manager.users.urls')),
]
