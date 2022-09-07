from django.urls import path
from . import views

urlpatterns = [
	path('login/',views.loginPage,name='login'),
	path('logout/',views.logoutPage,name='logout'),
	path('register/', views.registerPage, name='register'),

	path('account/', views.userAccount, name='account'),
	path('edit-account/', views.editAccount, name='edit-account'),
	path('create-skill/', views.createSkill, name='create-skill'),
	path('update-skill/<str:pk>/', views.updateSkill, name='update-skill'),
	path('delete-skill/<str:pk>/', views.deleteSkill, name='delete-skill'),



	path('', views.profiles,name='user-profiles'),
	path('profile/<str:pk>/',views.userProfile,name='user-profile'),
]