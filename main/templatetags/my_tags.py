from django import template
from main.models import MenuItem
from django.urls import reverse


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name, active_url):
    menu_items = MenuItem.objects.filter(menu_name=menu_name).order_by('tree_id', 'level', 'name')
    context['menu_items'] = menu_items
    context['active_url'] = active_url
    return ''
