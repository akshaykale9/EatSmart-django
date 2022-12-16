from django.contrib import admin
from django.urls import path
from recommender import views

urlpatterns = [
    path("" ,views.home,name="home"),
    path("bodymass/",views.bodymass,name="bodymass"),
    path("dietplanner/",views.index,name="dietplanner"),
    path("diet/",views.diet,name="diet"),
    path("about/",views.about,name="about")
]