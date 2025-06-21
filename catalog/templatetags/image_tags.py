from django import template
from django.templatetags.static import static

register = template.Library()


@register.filter
def default_image(image_field):
    """
    Возвращает URL изображения, если оно есть.
    Иначе — путь к изображению-заглушке.
    """
    if image_field:
        return image_field.url
    return static('img/placeholder.png')
