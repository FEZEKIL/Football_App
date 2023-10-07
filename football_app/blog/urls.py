from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('specific', views.specific, name='specific'),

]

#https://apiv3.apifootball.com/?action=get_events&from=2023-04-05&to=2023-04-05&league_id=152&APIkey=9b622f7d1cba87ae4e6dcc24827bd27db9f031d4c51c527c24f76a1545722894