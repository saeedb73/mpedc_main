from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from project.models import Project, Report


# Create your views here.
@login_required(login_url='loginuser')
def home(request):
    if request.user.is_superuser:
        projects = Project.objects.all()
        number_of_projects = Project.objects.count()
        number_of_normal_projects = 0
        number_of_warner_projects = 0
        number_of_dangerous_projects = 0
        for project_item in projects:
            if project_item.check_variable() <= 1:
                number_of_normal_projects += 1
            elif project_item.check_variable() <= 1.1:
                number_of_warner_projects += 1
            else:
                number_of_dangerous_projects += 1
    else:
        projects = Project.objects.filter(user=request.user)
        number_of_projects = Project.objects.filter(user=request.user).count()
        number_of_normal_projects = 0
        number_of_warner_projects = 0
        number_of_dangerous_projects = 0
        for project_item in projects:
            if project_item.check_variable() <= 1:
                number_of_normal_projects += 1
            elif project_item.check_variable() <= 1.1:
                number_of_warner_projects += 1
            else:
                number_of_dangerous_projects += 1
    return render(request, 'project/home.html', {'projects': projects, 'number_of_projects': number_of_projects, 'number_of_normal_projects': number_of_normal_projects,
                                                 'number_of_warner_projects': number_of_warner_projects, 'number_of_dangerous_projects': number_of_dangerous_projects})


@login_required(login_url='loginuser')
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    reports = Report.objects.filter(project=project)
    return render(request, 'project/project_detail.html', {'project': project, 'reports': reports})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'project/loginuser.html')
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'project/loginuser.html', {'error': "نام کاربری یا پسورد ایراد دارد."})
        else:
            login(request, user)
            return redirect('home')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')
