from django.urls import path

from . import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', views.AccountViewSet, basename='accounts')

# router.register(r'head_officers/profiles', views.HeadProfileViewSet, basename='head_officer_profiles')
# router.register(r'accounts/users/<str:username>/profile/', views.HeadProfileDetailView, basename='head_officer_profile_detail')

# router.register(r'officers/profiles', views.OfficerProfileViewSet, basename='officer_profiles')
# router.register(r'officers/<str:username>/profile/', views.OfficerProfileDetailView, basename='officer_profile_detail')

# router.register(r'scholars/profiles', views.ScholarProfileViewSet, basename='scholar_profiles')
# router.register(r'head_officers/<str:username>/profile/', views.OfficerProfileDetailView, basename='officer_profile_detail')

urlpatterns = [
    path('', views.login, name="login"),
    # path('users/<str:username>/profile/', views.UserProfileDetailView.as_view(), name='user_profile'),

    path('users/head_officers/', views.HeadList.as_view(), name='list_all_head_officers'),
    path('users/head_officers/<str:username>/profile/', views.HeadProfileDetailView.as_view(), name='view_head_officer_profile'),

    path('users/officers/', views.OfficerList.as_view(), name='list_all_officers'),
    path('users/officers/<str:username>/profile/', views.OfficerProfileDetailView.as_view(), name='view_officer_profile'),

    path('users/scholars/', views.ScholarList.as_view(), name='list_all_scholars'),
    path('users/scholars/<str:username>/', views.AccountDetailView.as_view(), name='scholar_profile'),
    path('users/scholars/<str:username>/profile/', views.ScholarProfileDetailView.as_view(), name='view_scholar_profile'),
] + router.urls