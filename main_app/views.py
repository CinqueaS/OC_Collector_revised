from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .models import Story 
from .forms import ChapterForm

class Home(LoginView):
    template_name = 'home.html'

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class StoryUpdate(UpdateView):
    model = Story
    fields = ['title', 'chapters', 'synopsis']

class StoryDelete(DeleteView):
    model = Story
    success_url = '/stories/'