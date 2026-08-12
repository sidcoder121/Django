import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Task

def home(request):
    """Renders the main page with all existing tasks."""
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'tasks': tasks})

@require_http_methods(["POST"])
def add_task(request):
    """Handles creating a new task via AJAX."""
    try:
        data = json.loads(request.body)
        title = data.get('title', '').strip()
        
        if not title:
            return JsonResponse({'error': 'Task title cannot be empty'}, status=400)

        task = Task.objects.create(title=title)
        return JsonResponse({
            'id': task.id,
            'title': task.title
        }, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["DELETE"])
def delete_task(request, task_id):
    """Handles removing a task via AJAX."""
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=200)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)