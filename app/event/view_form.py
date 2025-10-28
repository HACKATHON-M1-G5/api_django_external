from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app.event.models import Event
from app.category.models import Category
from django.utils.dateparse import parse_datetime

@csrf_exempt
def add_event(request):
    if request.method == "POST":
        data = json.loads(request.body)
        category_id = data.get("category")
        category = Category.objects.get(id=category_id)

        event = Event.objects.create(
            category=category,
            name=data.get("name", ""),
            start_at=parse_datetime(data.get("start_at")),
            end_at_expected=parse_datetime(data.get("end_at_expected")),
            status=data.get("status", "pending"),
            score=data.get("score")
        )
        return JsonResponse({
            "id": event.id,
            "name": event.name,
            "category": event.category.id,
            "start_at": str(event.start_at),
            "end_at_expected": str(event.end_at_expected),
            "status": event.status,
            "score": event.score
        })
    return JsonResponse({"detail": "Method not allowed"}, status=405)
