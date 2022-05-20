from django import template
import string
register = template.Library()


@register.filter
def cut_football(value):
    """Removes all values of arg from the given string"""
    value = value.replace("football", '')
    return value


@register.filter
def cut_others(value):
    chars = []
    for c in value:
        chars += [c]
    for c in chars:
        if not (c == " " or c in string.punctuation or c in string.ascii_letters or c in "0123456789"):
            value = value.replace(c, '')
    return value


@register.filter
def is_video(link):
    return "youtube" in link


@register.filter
def embedify(link):
    return link.replace('watch?v=', 'embed/', 1)
