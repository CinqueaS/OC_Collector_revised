from django.shortcuts import render
from .models import Story 

def home(request):
    return render(request, 'home.html')

def story_index(request):
    stories = Story.objects.all()
    return render(request, 'stories.html', {'stories': stories})

def story_detail(request, story_id):
    story = Story.objects.get(id=story_id)
    return render(request, 'stories/detail.html', {'story': story})
