from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, base64
from CoverMaker import coverMake  # Импортируйте вашу функцию

@csrf_exempt  # Отключаем CSRF для упрощения (в реальных приложениях используйте CSRF-токены)
def process_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Получаем JSON-данные из запроса
            print(data)
            pdf_content = coverMake(data)  # Вызываем вашу функцию с переданными данными
            return JsonResponse({"status": "success", "content": base64.b64encode(pdf_content).decode("utf-8")})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})