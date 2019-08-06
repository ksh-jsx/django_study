from django.shortcuts import render
from django.utils import timezone
from .models import Post,Tags,Comment,CustomUser,Items
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,TagForm,CommentForm,CustomUserCreationForm,find_userForm
from django.shortcuts import redirect
from django.db.models import F,Count
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.urls import reverse_lazy
from django.views import generic
from django.conf import settings
from django.views.generic.base import TemplateView, View
from django.middleware.csrf import _compare_salted_tokens
from blog.oauth.providers.naver import NaverLoginMixin
from django.http import HttpResponseRedirect,HttpResponse


def main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'baangbang/main.html', {'posts': posts})

def search_univ(request):
    q = request.GET.get('q', '')
    item = Items.objects.filter(loca=q)
    return render(request, 'baangbang/search_for_sale.html', {'info': q, 'item':item})

def find_username(request):
    if request.method == "POST":
        form = find_userForm(request.POST)
        post = form.save(commit=False)
        posts = CustomUser.objects.filter(name=post.name, email=post.email).values('username', 'name')
    
        if posts:
            return render(request, 'registration/find_username.html', {'form': '키미노 ID와 "'+posts[0]['username']+'" 데스'}) 
        else:
            invalid = "존재하지않는 정보입니다."
            return render(request, 'registration/find_username.html', {'form': invalid}) 
    else:
        form = find_userForm()
        return render(request, 'registration/find_username.html', {'form': form}) 
        #없는 정보일때 오류남

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

 
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup_success')
    template_name = 'registration/signup.html'


def test(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('test')
    else:
        form = TagForm()

    test = Tags.objects.all().values('tag').annotate(total=Count('tag')).order_by('-total')[:5]
    return render(request, 'blog/test.html', {'test': test,'form' : form})



@login_required
def email_to_admin(request):
    userId = request.user
    
    return render(request, 'admin/email.html', {'userId': userId, 'test':request.META['HTTP_USER_AGENT']})

@login_required
def payment(request):
    user = CustomUser.objects.all()
    return render(request, 'admin/payment.html', {'user_info': user})

class SocialLoginCallbackView(NaverLoginMixin, View):

    success_url = settings.LOGIN_REDIRECT_URL
    failure_url = settings.LOGIN_URL
    required_profiles = ['email', 'name']

    model = get_user_model()

    def get(self, request, *args, **kwargs):

        provider = kwargs.get('provider')
        success_url = request.GET.get('next', self.success_url)

        if provider == 'naver':
            csrf_token = request.GET.get('state')
            code = request.GET.get('code')
            if not _compare_salted_tokens(csrf_token, request.COOKIES.get('csrftoken')):
                messages.error(request, '잘못된 경로로 로그인하셨습니다.', extra_tags='danger')
                return HttpResponseRedirect(self.failure_url)
            is_success, error = self.login_with_naver(csrf_token, code)
            if not is_success:
                messages.error(request, error, extra_tags='danger')
            return HttpResponseRedirect(success_url if is_success else self.failure_url)

        return HttpResponseRedirect(self.failure_url)

    def set_session(self, **kwargs):
        for key, value in kwargs.items():
            self.request.session[key] = value

