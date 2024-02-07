from django.contrib import admin
from django.urls import path, include
from task_manager.views import IndexPageView, LoginUserView, LogoutUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('users/', include('task_manager.users.urls')),
#    path('statuses/', include('task_manager.statuses.urls')),
]
