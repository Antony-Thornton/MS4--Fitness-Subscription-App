from django import template

register = template.Library()


@register.filter(name='sub_total')
def sub_total(price, quantity):
    return price * quantity