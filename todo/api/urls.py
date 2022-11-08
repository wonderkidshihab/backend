from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


from .views import TodoView, TodoModelView

urlpatterns = [
    path("todo/", TodoView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("todo/<int:pk>/", TodoModelView.as_view()),
]
