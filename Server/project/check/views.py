# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# from django.contrib.auth.models import User
from .models import CaseFiles
from apply.models import Case
from authentication.views import group_required

import json
import os
import shutil
import datetime
# Create your views here.


@group_required('Volunteer', 'Engineer')
def home(request):
    path = os.path.abspath('.') + "/templates/check.html"
    return render(request, path)


@group_required('Volunteer')
def upload(request):
    SN = request.POST.get('sn')
    uploadFiles = request.FILES.getlist('file')

    if CaseFiles.objects.filter(SN=SN):
        if Case.objects.get(SN=SN).assign == '1' and Case.objects.get(SN=SN).volunteer == request.user.username:
            fs = FileSystemStorage()
            path = os.path.abspath('.') + "/uploads"
            destination = CaseFiles.objects.get(SN=SN).path

            for f in uploadFiles:
                if f.name.endswith('.html'):
                    fs.save('result'+SN+'.html', f)
                else:
                    fs.save(f.name, f)

            for f in os.listdir(destination):
                os.remove(destination + "/" + f)

            for f in os.listdir(path):
                shutil.move(path + "/" + f, destination)

            Case.objects.filter(SN=SN).update(checked='1',
                                              status=request.POST.get('status'),
                                              checkDate=datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

            return HttpResponse(json.dumps({'statusCode': 'success'}),
                                content_type="application/json")

        else:
            if Case.objects.get(SN=SN).assign == '0':
                return HttpResponse(json.dumps({'statusCode': 'case not assigned'}),
                                    content_type="application/json")
            if Case.objects.get(SN=SN).volunteer != request.user.username:
                return HttpResponse(json.dumps({'statusCode': 'permission denied'}),
                                    content_type="application/json")
    else:
        return HttpResponse(json.dumps({'statusCode': 'case not found'}),
                            content_type="application/json")


@group_required('Volunteer', 'Engineer')
def result(request):
    SN = request.POST.get('sn')
    if CaseFiles.objects.filter(SN=SN):
        if Case.objects.get(SN=SN).volunteer == request.user.username or request.user.groups.filter(name="Engineer").exists() is True or request.user.is_superuser is True:
            if Case.objects.get(SN=SN).checked == '1':
                case = CaseFiles.objects.get(SN=SN)
                if os.path.isfile(case.path + "/result" + SN + ".html") is True:
                    # return render(request, case.path + "/result" + SN + ".html")

                    # respond with an attachment
                    openFile = open(case.path + "/result" + SN + ".html", 'r')
                    response = HttpResponse(openFile.read(), content_type="text/html")
                    response['Content-Disposition'] = 'attachment; filename="result' + SN + '.html"'
                    return response
                else:
                    return HttpResponse(json.dumps({'statusCode': 'file does not exist'}),
                                        content_type="application/json")
            else:
                return HttpResponse(json.dumps({'statusCode': 'case not checked'}),
                                    content_type="application/json")
        else:
            return HttpResponse(json.dumps({'statusCode': 'permission denied'}),
                                content_type="application/json")
    else:
        return HttpResponse(json.dumps({'statusCode': 'case not found'}),
                            content_type="application/json")


@group_required('Volunteer', 'Engineer')
def showUnassignedCases(request):
    data = Case.objects.filter(assign='0')
    response = []
    for d in data:
        response.append(d.SN + " " + d.name)
    return HttpResponse(response)


@group_required('Volunteer')
def volunteerShowCheckedCases(request):
    data = Case.objects.filter(volunteer=request.user.username, checked='1')
    response = []
    for d in data:
        response.append('<ul id="' + d.SN + '">')
        response.append('<li id="sn">' + d.SN +'</li>')
        response.append('<li id="name">' + d.name + '</li>')
        response.append('</ul>')
    return HttpResponse(response)


@group_required('Volunteer')
def volunteerShowNotCheckedCases(request):
    data = Case.objects.filter(volunteer=request.user.username, checked='0')
    response = []
    for d in data:
        response.append(d.SN + " " + d.name + " " + d.address)
    return HttpResponse(response)


@group_required('House', 'Volunteer')
def personalShowAppliedCases(request):
    data = Case.objects.filter(username=request.user.username)
    response = []
    for d in data:
        response.append('<ul id="' + d.SN + '">')
        response.append('<li id="sn">' + d.SN + '</li>')
        response.append('<li id="name">' + d.address + '</li>')
        response.append('<li id="checked">' + d.checked + '</li>')
        response.append('</ul>')
    return HttpResponse(response)


@group_required('Engineer')
def engineerShowChecks(request):
    data = Case.objects.filter(checked='1')
    response = []
    for d in data:
        response.append(d.SN + " " + d.name + " " + d.address)
    return HttpResponse(response)


@group_required('Volunteer', 'Engineer')
def showDetail(request):
    if Case.objects.filter(SN=request.POST.get('sn')):
        case = Case.objects.get(SN=request.POST.get('sn'))
        response = []
        response.append(case.SN)
        response.append(case.name)
        response.append(case.buildingType)
        response.append(case.address)
        response.append(case.phone)
        response.append(case.applyDate)
        return HttpResponse(response)
    else:
        return HttpResponse(json.dumps({'statusCode': 'case not found'}),
                            content_type="application/json")


@group_required('Volunteer')
def assign(request):
    SN = request.POST.get('sn')
    if Case.objects.filter(SN=SN):
        if Case.objects.get(SN=SN).assign == '0':
            Case.objects.filter(SN=SN).update(volunteer=request.user.username,
                                              assign='1')
            return HttpResponse(json.dumps({'statusCode': 'success'}),
                                content_type="application/json")
        else:
            return HttpResponse(json.dumps({'statusCode': 'case was assigned'}),
                                content_type="application/json")
    else:
        return HttpResponse(json.dumps({'statusCode': 'case not found'}),
                            content_type="application/json")
