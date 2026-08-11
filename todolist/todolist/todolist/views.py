from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
import json

def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title', '').strip()
        if title:
            task = Task.objects.create(title=title)
            return JsonResponse({'status': 'success', 'id': task.id, 'title': task.title})
    return JsonResponse({'status': 'error'}, status=400)

def delete_task(request, task_id):
    if request.method == 'DELETE':
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return JsonResponse({'status': 'success'})
        except Task.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)
    return JsonResponse({'status': 'error'}, status=400)