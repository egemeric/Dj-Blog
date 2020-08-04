from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views, apiviews

# router = routers.DefaultRouter()
# router.register(r'coments', views.CommentViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('get/<int:content_id>', views.dynamic, name='dynamic'),
    path('post_dt/', views.update_post, name='update_post'),
    path('create_post/', views.create_new_post, name='create_new_post'),
    path('create_post_panel/', views.create_new_post_panel, name='create_new_post_panel'),
    path('get/<int:content_id>/edit/', views.edit_full_post, name='edit'),
    path('get/<int:content_id>/delete/', views.delete_post, name='delete_post'),
    path('api/', apiviews.CommentList.as_view(), name='comment_list'),
    path('api/get/<int:pk>', apiviews.CommentDetail.as_view(), name='comment_detail'),
    path('users/', apiviews.UserList.as_view()),
    path('users/<int:pk>/', apiviews.UserDetail.as_view()),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
