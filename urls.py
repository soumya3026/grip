from django.urls import path

from . import views

app_name='bbs'
urlpatterns=[
   path('',views.index,name="index"),
   path('show',views.show,name="show"),
   path('detail',views.detail,name="detail"),    
   ]