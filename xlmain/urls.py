from django.urls import path
from . import views

urlpatterns=[
    path("",views.home),
    path("cse",views.cse),
    path("ece",views.ece),
    path("mech",views.mech),
    path("civil",views.civil),
    path("chem",views.chem),
    path("mme",views.mme),
]

