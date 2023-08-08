from django.urls import path
from profile_app import views

urlpatterns = [
    path('', views.ProfileList.as_view(), name='profile_list'),
    path('p/<int:pk>', views.ProfileView.as_view(), name='profile_view'),
    path('', views.ProfileCreate.as_view(), name='profile_new'),
    path('/<int:pk>', views.ProfileUpdate.as_view(), name='profile_edit'),
    path('p/<int:pk>', views.ProfileDelete.as_view(), name='profile_delete'),
]