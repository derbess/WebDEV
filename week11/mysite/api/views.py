from django.shortcuts import render
from .models import TaskList
from django.http import JsonResponse

# Create your views here.
def showTaskLists(request):
    arr = TaskList.objects.all()
    jsonData = [l.to_json() for l in arr]
    return JsonResponse(jsonData, safe=False)

def task_list(request, pk):
    try:
        t_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    return JsonResponse(t_list.to_json(), safe=False)


def task_lists(request, pk):
    try:
        t_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    tasks = t_list.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)