from django.urls import path,include
from .views import UserAPIView,UserfavAPIView
urlpatterns = [
    path('' ,UserAPIView.as_view()),
    path('users_fav',UserfavAPIView.as_view()),
]