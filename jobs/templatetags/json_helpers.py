from django import template

register = template.Library()


@register.assignment_tag
def get_value(data, key):
    return data[key]