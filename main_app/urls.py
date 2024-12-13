from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('stories/', views.story_index, name='stories'),
    path('stories/<int:story_id>/', views.story_detail, name='story-detail' ),
    path('stories/create/', views.StoryCreate.as_view(), name='story-create'),
    path('stories/<int:pk>/update/', views.StoryUpdate.as_view(), name='story-update'),
    path('stories/<int:pk>/delete/', views.StoryDelete.as_view(), name='story-delete'),
    path('stories/<int:story_id>/add-chapter', views.add_chapter, name='add-chapter' ),
    path('accounts/signup/', views.signup, name='signup'),
]