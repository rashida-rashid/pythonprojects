from django.urls import path
from .import views

app_name='searchapp'

urlpatterns=[
    path('searchapp/',views.searchresult,name='searchresult')
]