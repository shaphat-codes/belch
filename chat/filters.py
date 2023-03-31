from . models import *
import django_filters

class MessageFilter(django_filters.FilterSet):
    class Meta:
        model = Message
        fields = ['message', 'time', 'receiver', 'sender', 'room_name', 'id']


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['id', 'username']