"""Circles views."""

# Django
from django.http import JsonResponse

# Models
from cride.circles.models import Circle

def list_circles(request):
    """List circles."""
    circles = Circle.objects.all()
    data = []
    for circle in circles:
        print('---->', circle)
    return JsonResponse('Hola', safe=False)