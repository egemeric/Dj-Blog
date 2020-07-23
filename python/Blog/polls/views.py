from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Comment
from .forms import CommentForm


def index(request):
    latest_comment_list = Comment.objects.order_by('-Pub_date')[:]
    context = {'latest_cmt_list': latest_comment_list, 'request': request}
    print(request.headers)
    print(request.user)
    return render(request, 'index.html', context)


def dynamic(request, content_id):
    try:
        cmt=Comment.objects.get(pk=content_id)
    except:
        raise Http404("Not Found")

    if request.user.is_authenticated:
        context = {'cmt': cmt,'user': request.user, 'auth_user': True}
        return render(request, 'details.html', context)
    else:
        context = {'cmt': cmt, 'auth_user': False}
        return render(request, 'details.html', context)


def update_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            post_id = request.POST.get('post_id')
            post_data = request.POST.get('update_post')
            try:
                cmt = Comment. objects.get(pk=int(post_id))
                cmt.Content = post_data
                cmt.save(update_fields=['Content'])
                context={'cmt': cmt.id}
            except Comment.DoesNotExist:
                return HttpResponse(status=500)

        return render(request, 'post.html', context)
    else:
        return HttpResponse('Unauthorized', status=401)


def create_new_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'create.html')
    else:
        return HttpResponse('Unauthorized', status=401)


def create_new_post_panel(request):
    form = CommentForm()
    return render(request, 'create.html', {'form': form})


