from django.urls import path,re_path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^email_to_admin/$', views.email_to_admin, name='email_to_admin'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup_success/', TemplateView.as_view(template_name='registration/signup_success.html'), name='signup_success'),
    path('test', views.test, name='test'),
]

