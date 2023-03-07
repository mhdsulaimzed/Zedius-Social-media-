from django.urls import path
from wallpage import views



urlpatterns = [
    path("signup",views.SignupView.as_view(),name="sign-up"),
    path("signin",views.SigninView.as_view(),name="log-in"),
    path("home",views.IndexView.as_view(),name="home"),
    path("profile/add",views.UserProfileCreateView.as_view(),name="profile-add"),
    path("profile/edit/<int:id>",views.UserProfileUpdateView.as_view(),name="profile-edit"),
    path("signout",views.SignoutView.as_view(),name="log-out"),
    path('post/<int:id>/remove',views.PostDeleteView.as_view(),name="post-remove"),
    path('profile',views.UserProfileView.as_view(),name="profile-view"),
    path('profile/<int:id>/view',views.CommonUserProfile.as_view(),name="user-pro"),
    path("post/like/<int:id>",views.LikesViews.as_view(),name="like"),
    path("post/<int:id>/comment",views.CommentView.as_view(),name="comment"),
    path("comments/like/<int:id>",views.CommentLikesViews.as_view(),name="c-like"),
    path("user/profile/<int:id>/addfollowes",views.AddFollowers.as_view(),name="add-follower"),
    path("user/profile/<int:id>/removefollowes",views.RemoveFollowers.as_view(),name="rmv-follower"),
    path("user/comments/<int:id>/remove",views.CommentRemove.as_view(),name="com-remove")
   

   ]