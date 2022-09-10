from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('<str:login>/',views.login,name='login'),
    path('<str:login>/<int:forget>/',views.forget,name='forget'),
    path('<str:login>/<str:signup>/',views.signup,name='signup'),
    path('<str:login>/<int:forget>/<int:update>/',views.update,name='update'),
    path('<str:login>/<str:signup>/<int:q_id>/',views.checking,name='checking'),
    path('<str:login>/<str:signup>/<str:index>/',views.index,name='index'),
    path('<str:login>/<str:signup>/<str:index>/<int:question_id>/', views.detail, name='detail'),
    path('<str:login>/<str:signup>/<str:index>/<int:question_id>/<int:form_id>/',views.finalpage, name='finalpage'),
]

