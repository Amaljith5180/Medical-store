from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('login/',views. login_view, name='login'),
    path('add_medicine/',views. add_medicine_view, name='add_medicine'),
    path('medicine_list/',views. medicine_list_view, name='medicine_list'),
     path('medicine/<int:pk>/edit/',views. edit_medicine_view, name='edit_medicine'),
    path('medicine/<int:pk>/delete/',views. delete_medicine_view, name='delete_medicine'),
    path('logout/', views.logout_view,name='logout'),
    path('edit_medicine/<int:pk>/', views.edit_medicine_view, name='edit_medicine'),
    path('delete_medicine/<int:pk>/', views.delete_medicine_view, name='delete_medicine'),
      
    
]
