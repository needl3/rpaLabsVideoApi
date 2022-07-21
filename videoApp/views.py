from django.http import HttpResponse
from django.shortcuts import render
from . import models


def index(request):
    return render(request, "videoApp/upload.html")
    return render(request, "videoApp/index.html", {"videos": models.Video.objects.all()})
