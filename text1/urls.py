from django.urls import path
from text1 import views
urlpatterns = [
    path("user_view/", views.UserView.as_view()),
    path("user_view/<str:id>/", views.UserView.as_view()),
    path("user_drf/", views.StudentAPIView.as_view()),
    path("user_drf/<str:id>/", views.UserView.as_view()),

]