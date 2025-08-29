import calendar
from django import template
from django.utils.translation import gettext as _

register = template.Library()

@register.filter
def month_name(month_number):
  return _(calendar.month_name[month_number])