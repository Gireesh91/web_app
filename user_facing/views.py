from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AndroidApp, UserProfile, Task
from django import forms

class ScreenshotForm(forms.Form):
    screenshot = forms.ImageField()


@login_required
def apps_and_points(request):
    apps = AndroidApp.objects.all()
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'apps': apps,
        'points': user_profile.points_earned
    }
    return render(request, 'apps_and_points.html', context)

@login_required
def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'user_profile.html', context)

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.tasks_completed += 1
    user_profile.save()
    # Handle other task completion logic
    return redirect('apps_and_points')

@login_required
def upload_screenshot(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = ScreenshotForm(request.POST, request.FILES)
        if form.is_valid():
            screenshot = form.cleaned_data['screenshot']
            # Save the screenshot and associate it with the task
            task.screenshot = screenshot
            task.save()
            return redirect('apps_and_points')
    else:
        form = ScreenshotForm()
    context = {
        'form': form,
        'task': task
    }
    return render(request, 'upload_screenshot.html', context)
