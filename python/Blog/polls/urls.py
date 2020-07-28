from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'coments', views.CommentViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('get/<int:content_id>', views.dynamic, name='dynamic'),
    path('post_dt/', views.update_post, name='update_post'),
    path('create_post/', views.create_new_post, name='create_new_post'),
    path('create_post_panel/', views.create_new_post_panel, name='create_new_post_panel'),
    path('get/<int:content_id>/edit/', views.edit_full_post, name='edit'),
    path('get/<int:content_id>/delete/', views.delete_post, name='delete_post'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]