import re
from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def projectCreate(request):
	profile = request.user.profile
	form = ProjectForm()

	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			project = form.save(commit = False)
			project.owner = profile
			project.save()
			return redirect('account')
	context={'form':form}
	return render(request, 'projects/project_form.html',context)

@login_required(login_url='login')
def projectUpdate(request,pk):
	profile = request.user.profile
	project = profile.project_set.get(id = pk)
	form = ProjectForm(instance=project)
	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES, instance=project)
		if form.is_valid():
			form.save()
			return redirect('account')
	context = {'form': form}
	return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def projectDelete(request, pk):
	profile = request.user.profile
	project = profile.project_set.get(id = pk)
	if request.method == 'POST':
		project.delete()
		return redirect('account')
	context = {'object':project}
	return render(request, 'delete_object.html',context)

def projects(request):
	projectsList = Project.objects.all()
	return render(request, 'projects/projects.html', context={'projects':projectsList})

def project(request, pk):
	projectObj = Project.objects.get(id=pk)
	return render(request, 'projects/project.html', context={'projectObj':projectObj})
