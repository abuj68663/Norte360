from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, JsonResponse, Http404


def about(request):
    return render(request, 'about.html')


def promote(request):
    return render(request, 'promote.html')


def home(request):
    post = Upload.objects.all().order_by('-date')

    context = {
        'post': post,
    }
    return render(request, 'home.html', context)


def base(request):
    alup = Upload.objects.all()

    return {'alup': alup,}


def search(request):
    query = request.GET.get('myCountry')

    audio = Upload.objects.filter(title__icontains=query)

    context = {
        'audio': audio,
    }
    return render(request, 'search.html', context)


def crypto(request):
    post = Upload.objects.filter(category='Crypto').order_by('-date')

    context = {
        'post': post,
    }
    return render(request, 'crypto.html', context)


def videos(request):
    post = Upload.objects.filter(category='Videos').order_by('-date')

    context = {
        'post': post,
    }
    return render(request, 'video.html', context)


def song(request):
    post = Upload.objects.filter(category='Music').order_by('-date')

    context = {
        'post': post,
    }
    return render(request, 'post.html', context)


def post_details(request, pk):
    post = Upload.objects.get(pk=pk)

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip = get_ip(request)

    if ViewCount.objects.filter(ip=ip).exists():
        post.views.add(ViewCount.objects.get(ip=ip))

    else:
        ViewCount.objects.create(ip=ip)
        post.views.add(ViewCount.objects.get(ip=ip))

    comments = Comment.objects.filter(post=post).order_by('date')

    # Comments Form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.save()
            return HttpResponseRedirect(reverse('post-details', args=[pk]))
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'total_views': post.total_views(),
    }
    return render(request, 'post-details.html', context)


