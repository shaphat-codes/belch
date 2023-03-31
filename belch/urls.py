
from django.contrib import admin
from django.urls import path, include
from chat.views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path(('users/'), include('users.urls')),

    path('messages/', MessagesView, name = "messages"),
    path('userslist/', UserList, name = "users"),
    path('messages-create/', MessagesCreate, name = "messages-create"),

]
