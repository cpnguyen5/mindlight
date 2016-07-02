from django.db.models import Count
from django.conf import settings

from dashing.widgets import NumberWidget, ListWidget, GraphWidget

from random import randint

class CustomWidget(NumberWidget):
    title = 'My Custom Widget'
    value = 25

    def get_more_info(self):
        more_info = 'Random additional info'
        return more_info




users = randint(50, 100)


class NewClientsWidget(NumberWidget):
    title = 'New Users'

    def get_value(self):
        global users
        users += 1
        return users

    def get_detail(self):
        global users
        return '{} actives'.format(users / 3)

    def get_more_info(self):
        global users
        return '{} fakes'.format(users / 10)