from django.urls import path

from devsearch.settings import MEDIA_ROOT
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',views.projects,name='projects'),
	path('project/<str:pk>/',views.project,name='project'),
	path('create-project/',views.projectCreate,name='create-project' ),
	path('update-project/<str:pk>/',views.projectUpdate,name='update-project'),
	path('delete-project/<str:pk>/',views.projectDelete,name='delete-project'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)