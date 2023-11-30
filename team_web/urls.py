from django.urls import path
from . import views

#Defines all urls associated with the web app.

urlpatterns = [
    path('', views.home, name='home'),
    path('teammember/<int:id>', views.update_team_member, name='teammember'),
    path('add_teammember/', views.add_team_member, name='add_team_member'),
    path('delete_teammember/<int:id>', views.delete_team_member, name='delete_team_member'),
]