from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Story 
from .forms import ChapterForm

def home(request):
    return render(request, 'home.html')

def story_index(request):
    stories = Story.objects.all()
    return render(request, 'stories.html', {'stories': stories})

def story_detail(request, story_id):
    story = Story.objects.get(id=story_id)
    chapter_form = ChapterForm()
    return render(request, 'stories/detail.html', {'story': story, 'chapter_form': chapter_form})

def add_chapter(request, story_id):

    form = ChapterForm(request.POST)

    if form.is_valid():

        new_chapter = form.save(commit=False)
        new_chapter.story_id = story_id
        new_chapter.save()
    return redirect('story-detail', story_id=story_id)



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