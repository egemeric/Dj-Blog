from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .forms import CommentForm
from .serializers import CommetSerializer

class CommentAPI(APIView):
    def get(self, request):
        cmt=Comment.objects.all()
        serializer=CommetSerializer(cmt, many=True)
        return Response(serializer.data)
    def post(self):
        pass
def index(request, req_page=0):
    item_ct=Comment.objects.count()
    page_count = int(item_ct / 5)
    latest_comment_list = Comment.objects.order_by('-Pub_date')[req_page*5:(req_page*5)+5]
    context = {'latest_cmt_list': latest_comment_list,
               'request': request,
               'page_count': page_count+1,
               'current_page': req_page,
               'next_page': req_page+1,
               }
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
                cmt = Comment.objects.get(pk=int(post_id))
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
                form=form.save(commit=False)
                form.Ip_log = request.META['REMOTE_ADDR']
                form.User_agent = request.META['HTTP_USER_AGENT']
                form.save()
                item_ct=Comment.objects.count()
                return redirect('/')
            else:
                return HttpResponse('Form is not valid')
        else:
            return HttpResponse('Http Method ERROR')
    else:
        return HttpResponse('Unauthorized, Yetkin yok :D', status=401)


def create_new_post_panel(request):
    form = CommentForm()
    return render(request, 'create.html', {'form': form})


def edit_full_post(request, content_id):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized, Yetkin Yok :D', status=401)
    cmt = Comment.objects.get(pk=int(content_id))
    if request.method == 'POST':
        form=CommentForm(request.POST, request.FILES, instance=cmt)
        if form.is_valid():
            cmt = form.save(commit=False)
            cmt.Pub_date = timezone.now()
            cmt.Ip_log = request.META['REMOTE_ADDR']
            cmt.User_agent = request.META['HTTP_USER_AGENT']
            cmt.save()
            return redirect('/pools/get/'+str(cmt.id))
        else:
            return HttpResponse("Form is not valid!")
    else:
        form=CommentForm(instance=cmt)
        return render(request,'edit_post.html', {'form': form, 'cmt': cmt})


def delete_post(request,content_id):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized, Yetkin Yok :D', status=401)
    cmt = Comment.objects.get(pk=content_id)
    if request.method == 'GET':
        return render(request, 'delete_post.html', {'cmt': cmt})
    elif request.method == 'POST':
        check_again = request.POST.get('ask_yes')
        if check_again == str(check_again).lower() == 'yes':
            cmt.delete()
            return redirect('/')
        else:
            return HttpResponse("Please write yes to delete!")
    else:
        return HttpResponse('Http method error')


