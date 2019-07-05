from django.shortcuts import render,redirect
from .models import Taskmate
from .forms import Taskform
# Create your views here.
def todolist(request):
	if request.method == 'POST':
		form = Taskform(request.POST or None)
		if form.is_valid():
			form.save()
		return redirect('todolist')
	else:
		all_task = Taskmate.objects.all
		return render(request, 'todolist.html', {'all_task':all_task})

def delete_task(request, task_id):
	task = Taskmate.objects.get(pk=task_id)
	task.delete()
	return redirect('todolist')


def completed_task(request, task_id):
	task = Taskmate.objects.get(pk=task_id)
	task.done = True
	task.save()
	return redirect('todolist')

def pending_task(request, task_id):
	task = Taskmate.objects.get(pk=task_id)
	task.done = False
	task.save()
	return redirect('todolist')



def edit_task(request, task_id):
	if request.method == 'POST':
		task = Taskmate.objects.get(pk=task_id)
		form = Taskform(request.POST or None, instance = task)
		if form.is_valid():
			form.save()
		return redirect('todolist')
	else:
		edit_obj = Taskmate.objects.get(pk=task_id)
		return render(request, 'edit.html', {'edit_obj':edit_obj})

def contact(request):
	return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})