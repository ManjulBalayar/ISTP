from django import template

register = template.Library()

@register.filter(name='replace_underscore')
def replace_underscore(value):
    """Replace underscores in a string with spaces."""
    return value.replace('_', ' ')
