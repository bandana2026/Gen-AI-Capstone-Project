# Create your views here.
from django.shortcuts import render
from .models import UserInfo
from django.db import IntegrityError   # ✅ Important import

def user_list(request):
    users = UserInfo.objects.all()
    return render(request, 'commoninfo/user_list.html', {'users': users})


def addUserInfo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        uniqueID = request.POST.get('uniqueID')
        dob = request.POST.get('dob')

        try:
            UserInfo.objects.create(
                name=name,
                uniqueID=uniqueID,
                dob=dob
            )

            return render(request, 'commoninfo/add.html', {'success': True})

        except IntegrityError:
            return render(request, 'commoninfo/add.html', {'error': 'User ID already exists!'})

    return render(request, 'commoninfo/add.html')


def fetchUserInfo(request):
    user = None

    if request.method == 'POST':
        uniqueID = request.POST.get('uniqueID')
        user = UserInfo.objects.filter(uniqueID=uniqueID).first()

    return render(request, 'commoninfo/fetch.html', {'user': user})