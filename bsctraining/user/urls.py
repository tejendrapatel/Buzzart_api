from django.urls import path,include
from user.views import *
from rest_framework.routers import DefaultRouter
from user import views

router =  DefaultRouter()
router.register('userapi',views.userModelViewSet,basename='user')

urlpatterns = [
    path('signup/',SIGNUP, name='user'),
    path('user/', views.userModelViewSet.as_view()),
]