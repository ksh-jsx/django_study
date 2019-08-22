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
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text

def main(request):

    if request.method == "POST":
        q = request.POST.get('usern', '')
        is_active = CustomUser.objects.filter(username=q).values('active', 'username')
        if is_active[0]['active']:
            return HttpResponse(
        '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
        'justify-content: center; align-items: center;">'
        '방올리기 페이지~~</span>'
        '</div>'
    )
        else:
            return render(request, 'baangbang/main.html', {'user_info': is_active[0]['active'] })
    else:
        return render(request, 'baangbang/main.html', {'user_info': 'asd'})

@login_required
def mail_authenticate(request):
    user = CustomUser.objects.filter(username='shkim787').values('auto_increment_id','email')
    print(user)
    current_site = get_current_site(request) 
    message = render_to_string('account/user_activate_email.html',{
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user[0]['auto_increment_id'])).decode('utf-8'),
        'token': account_activation_token.make_token(user),
    })
    mail_subject = "나누방 인증 메일입니다."
    user_email = user[0]['email']
    email = EmailMessage(mail_subject, message, to=[user_email])
    email.send()
    return HttpResponse(
        '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
        'justify-content: center; align-items: center;">'
        '입력하신 이메일<span>로 인증 링크가 전송되었습니다.</span>'
        '</div>'
    )
    return redirect('main')

@login_required
def activate(request, uid64, token):

    uid = force_text(urlsafe_base64_decode(uid64))
    user = CustomUser.objects.filter(auto_increment_id=uid).values('active', 'username')
    print(user)
    if user is not None :
        post = get_object_or_404(CustomUser, auto_increment_id=uid)
        post.active = True
        post.save()
        print(user)
        return redirect('/')
    else:
        return HttpResponse('비정상적인 접근입니다.')

def search_univ(request):
    q = request.GET.get('q', '')
    item = Items.objects.filter(loca=q)
    return render(request, 'baangbang/search_for_sale.html', {'info': q, 'item':item})

def item_detail(request):
    get_id = request.GET.get('item_id', '')
    detail = Items.objects.filter(auto_increment_id=get_id)
    return render(request, 'baangbang/item_detail.html', {'info': get_id, 'detail':detail})

@login_required
def payment(request):
    get_id = request.GET.get('item_id', '')
    detail = Items.objects.filter(auto_increment_id=get_id)
    return render(request, 'admin/payment.html', {'payment_info': detail})

def find_username(request):
    if request.method == "POST":
        form = find_userForm(request.POST)
        post = form.save(commit=False)
        posts = CustomUser.objects.filter(name=post.name, email=post.email).values('username', 'name')
    
        if posts:
            return render(request, 'registration/find_username.html', {'form': '당신의 ID는 "'+posts[0]['username']+'" 입니다.'}) 
        else:
            invalid = "존재하지않는 정보입니다."
            return render(request, 'registration/find_username.html', {'form': invalid}) 
    else:
        form = find_userForm()
        return render(request, 'registration/find_username.html', {'form': form}) 
       

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

