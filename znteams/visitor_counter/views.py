
from django.shortcuts import render
from .models import Visitor

def show_visitor_count(request):
    visitor_count = Visitor.objects.first()


    if visitor_count:
        visitor_count.count += 1
        visitor_count.save()

    return render(request, 'visitor_counter/visitor_count.html', {'visitor_count': visitor_count})
