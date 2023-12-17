from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tasks/',views.task_list),
    path('tasks/detail/',views.task_detail)
]