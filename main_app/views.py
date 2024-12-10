from django.shortcuts import render

class Story:
    def __init__(self, title, chapters, synopsis):
        self.title = title
        self.chapters = chapters
        self.synopsis = synopsis

stories = [
    Story('Dreamless', 12, "Dreamless is a fantasy story featuring the adventures of the greatest bounty hunter in the land, the Crimson Samurai - Haina Jina. Haina faces peril at every turn as he navigates the threat of a once thought extinguished villain's return"),
    Story('WitchKnight', 5, "WitchKnight synopsis"),
    Story('THB', 5, "THB synopsis")
]

def home(request):
    return render(request, 'home.html')

def story_index(request):
    return render(request, 'stories.html', {'stories': stories})