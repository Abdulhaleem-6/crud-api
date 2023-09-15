from django.urls import path
from . import views 

urlpatterns = [
    path('', views.PersonListCreateAPI.as_view()),
    path('<int:pk>/', views.PersonDetail.as_view()),
    path('<int:pk>/', views.PersonUpdateAPIView.as_view()),
    path('<int:pk>/', views.PersonDeleteAPIView.as_view())
]