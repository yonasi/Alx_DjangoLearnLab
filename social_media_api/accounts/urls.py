from django.urls import path
from .views import UsersRegistrationView, UserLoginView, TokenRetrieveView
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', UsersRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/', TokenRetrieveView.as_view(), name='token_retrieve'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]