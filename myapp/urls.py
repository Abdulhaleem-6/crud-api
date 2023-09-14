from django.urls import path
from . import views 

urlpatterns = [
    path('', views.PersonListCreateAPI.as_view()),
    path('<int:pk>/', views.PersonDetail.as_view()),
    path('<int:pk>/update/', views.PersonUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.PersonDeleteAPIView.as_view())
]