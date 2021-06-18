from django import template

register = template.Library()
from ..models import CSE

def range(value):
    return [1,2,3,4,5,6]
