from django.urls import path
from . views import (PublicDetailView, SignUpView, SignIn, SignOut, UsernameValidation, EmailValidation, VerificationView)
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

app_name = 'users'

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SignIn.as_view(), name='login'),
    path('logout/', SignOut.as_view(), name='logout'),
    path('profile/', views.profile_update_view, name='profile-update'),
    # path('logout/', views.logout_view, name='logout'),
    # path('login/', views.log_in, name='login'),
    path('public-profile/<int:pk>',
         PublicDetailView.as_view(), name='public_profile_view'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('remove/post/bookmark/<int:id>/', views.remove_saved_bookmark, name='remove-post-bookmark'),
    path('add/post/detail/bookmark/', views.add_bookmark_detail_page, name='add-post-bookmark-detail-page'),
    path('add/post/bookmark/', views.add_post_bookmark, name='add-post-bookmark'),
    path('follow/toggle/', views.follow_toggle, name='add-user-follow'),
    path('profile/bookmarks/', views.bookmarks_list, name='bookmarks-list'),
    path('validate/username/', csrf_exempt(UsernameValidation.as_view()), name="validate-username"),
    path('validate/email/', csrf_exempt(EmailValidation.as_view()), name="validate-email"),
    path('activate/<uidb64>/<token>/', VerificationView.as_view(), name="activate")
]
