from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),

    # All topics
    path('topics/', views.topics, name='topics'),

    # Current topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Add new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Add new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry")
]