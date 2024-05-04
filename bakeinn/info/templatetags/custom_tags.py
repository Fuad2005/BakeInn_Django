from django import template

register = template.Library()

@register.simple_tag
def remove_spaces(value):
    return value.replace(' ', '')