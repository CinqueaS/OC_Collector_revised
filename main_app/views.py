from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Story 

def home(request):
    return render(request, 'home.html')

def story_index(request):
    stories = Story.objects.all()
    return render(request, 'stories.html', {'stories': stories})

def story_detail(request, story_id):
    story = Story.objects.get(id=story_id)
    return render(request, 'stories/detail.html', {'story': story})


class StoryCreate(CreateView):
    model = Story
    fields = ['title', 'chapters', 'synopsis'] 
    success_url= '/stories/'

class StoryUpdate(UpdateView):
    model = Story
    fields = ['title', 'chapters', 'synopsis']

class StoryDelete(DeleteView):
    model = Story
    success_url = '/stories/'