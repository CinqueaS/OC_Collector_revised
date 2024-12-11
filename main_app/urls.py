from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stories/', views.story_index, name='stories'),
    path('stories/<int:story_id>/', views.story_detail, name='story-detail' ),
    path('stories/create/', views.StoryCreate.as_view(), name='story-create'),
    path('stories/<int:pk>/update/', views.StoryUpdate.as_view(), name='story-update'),
    path('stories/<int:pk>/delete/', views.StoryDelete.as_view(), name='story-delete'),
]