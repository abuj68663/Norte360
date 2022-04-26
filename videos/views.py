from django.shortcuts import render
from .models import *


def video(request):
    post = Videos.objects.all().order_by('-date')

    context = {
        'post': post,
    }
    return render(request, 'video.html', context)


def post_details(request, pk):
    post = Videos.objects.get(pk=pk)

    context = {
        'post': post,
    }
    return render(request, 'video-details.html', context)


