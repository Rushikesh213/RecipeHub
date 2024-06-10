from django.urls import path
from testapp.views import *

urlpatterns = [
    path('register/',register_page,name='register'),
    path('login/',login_page,name='login'),
    path('recipes_all',recipes_page,name='recipes'),
    path('logout',logout_page,name='logout'),
    path('delete/<int:pk>',recipes_delete,name='delete')

]
