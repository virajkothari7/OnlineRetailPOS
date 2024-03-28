from django.template import Library
from datetime import datetime

register = Library()
@register.filter()
def transactionID_2_date(value):
    return datetime.strptime(value, "%Y%m%d%H%M%S%f")

@register.filter()
def sort(value):
    return sorted(value,reverse=True)


