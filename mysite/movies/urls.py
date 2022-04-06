from django.urls import path
from .views import *
#MovieList,TheaterDetail,CityCreate,CityUpdate,CityList,CityDelete,CityDetail


urlpatterns = [
    #movie All work completed
    #path('',MovieList.as_view(), name='movies'), this is not required as we are showing it in Home page
    
    path('add_movie/',MovieCreate.as_view(), name='add_movie'),    
    path('movie/<slug:slug>',MovieDetail.as_view(), name='view_movie'),
    path('movie/update/<slug:slug>',MovieUpdate.as_view(), name='update_movie'),
    path('movie/delete/<slug:slug>',MovieDelete.as_view(), name='delete_movie'),

    path('add_city/',CityCreate.as_view(), name='add_city'),    
    path('city/<slug:slug>',CityDetail.as_view(), name='view_city'),
    path('city/update/<slug:slug>',CityUpdate.as_view(), name='update_city'),
    path('city/delete/<slug:slug>',CityDelete.as_view(), name='delete_city'),

    path('add_theater/',TheaterCreate.as_view(), name='add_theater'),
    path('theater/<slug:slug>',TheatherDetail.as_view(), name='view_theater'),
    path('theater/update/<slug:slug>',TheaterUpdate.as_view(), name='update_theater'),
    path('theater/delete/<slug:slug>',TheaterDelete.as_view(), name='delete_theater'),
    path('movie/<slug:slug>/book',bookmovie,name='book'),
]