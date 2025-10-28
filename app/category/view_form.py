from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app.category.models import Category

@csrf_exempt
def add_category(request):
    if request.method == "POST":
        data = json.loads(request.body)
        category = Category.objects.create(
            name=data.get("name", ""),
            description=data.get("description", "")
        )
        return JsonResponse({"id": category.id, "name": category.name, "description": category.description})
    return JsonResponse({"detail": "Method not allowed"}, status=405)
