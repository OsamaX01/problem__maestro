from django import template

register = template.Library()

@register.filter
def get_attribute(obj, name):
    return getattr(obj, name, u"")