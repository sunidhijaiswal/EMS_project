from django.urls import path 
from poll.views import *

urlpatterns = [
    path('',index,name='polls_list'),
    path('<int:id>/details/',details,name='details_page'),
    path('<int:id>/',poll,name='single_poll')
]