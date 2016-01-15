__author__ = 'jflaisha'

from django import template

register = template.Library()


@register.filter
def index(sequence, position):
    print sequence, position
    try:
        return sequence[position]
    except IndexError:
        # Django template logic is based on list with most items...
        # this except clause shows the last index item of shorter lists
        last_index = len(sequence) - 1
        return sequence[last_index]
