from django import template

register = template.Library()

@register.filter(name='attr')
def set_attr(field, attr_string):
    attr_name, attr_value = attr_string.split(':')
    field.field.widget.attrs[attr_name] = attr_value
    return field