from django.urls import path
from .import views

urlpatterns = [
    path('user-list/', views.userlist.as_view(), name='user_list'),
    path('user-create/', views.usercreate.as_view(), name='user_create'),
    path('user-retrive/<int:pk>/', views.userretrive.as_view(), name='user_retrive'),
    path('user-update/<int:pk>/', views.userupdate.as_view(), name='user_update'),
    path('user-destory/<int:pk>/', views.userdestory.as_view(), name='user_destory'),

]