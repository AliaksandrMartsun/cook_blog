from django import template
from contact.models import Social, About


register = template.Library()


@register.simple_tag()
def get_social_links():
    """Выводы ссылок соц. сетей"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """Выводы about"""
    return About.objects.last()