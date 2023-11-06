from .models import Visitor

def visitor_count(request):
    try:
        visitor = Visitor.objects.first()
        return {'visitor_count': visitor.count if visitor else 0}
    except Visitor.DoesNotExist:
        return {'visitor_count': 1}