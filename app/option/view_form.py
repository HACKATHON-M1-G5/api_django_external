from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app.option.models import Option

@csrf_exempt
def add_option(request):
    if request.method == "POST":
        data = json.loads(request.body)
        option = Option.objects.create(
            name=data.get("name", ""),
            value=data.get("value", "")
        )
        return JsonResponse({
            "id": option.id,
            "name": option.name,
            "value": option.value
        })
    return JsonResponse({"detail": "Method not allowed"}, status=405)
