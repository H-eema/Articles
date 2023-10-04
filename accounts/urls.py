from django.urls import path

from .views import UserArticleView, UserDetailView


urlpatterns = [
    path("<int:pk>/", UserArticleView.as_view(), name="user_detail"),
    path("<int:pk>/edit/", UserDetailView.as_view(), name="user_edit"),
]
