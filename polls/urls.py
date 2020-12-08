from polls.views import results
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:q_id>/results', views.results),
    path('vote/<int:ques_id>', views.vote),
    path('peepthis/<int:peep_id>', views.peep, name='peepthis')
]