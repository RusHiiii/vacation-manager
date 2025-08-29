from django import template

register = template.Library()

@register.filter
def mod(value, arg):
  try:
    return int(value) % int(arg)
  except (ValueError, ZeroDivisionError):
    return 0

@register.filter
def add(value, arg):
  try:
    return int(value) + int(arg)
  except (ValueError):
    return 0