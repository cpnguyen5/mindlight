from django.db.models import Count
from django.conf import settings

from dashing.widgets import NumberWidget, ListWidget, GraphWidget

class CustomWidget(NumberWidget):
    title = 'My Custom Widget'
    value = 25

    def get_more_info(self):
        more_info = 'Random additional info'
        return more_info