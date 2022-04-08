
from django.urls import path
from .views import TournamentsView,TournamentView,ContactView

urlpatterns = [
   path('',TournamentsView.as_view()),
    path('<int:pk>',TournamentView.as_view()),
      path('contact',ContactView.as_view()),
 
]