from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comments, Category
from . import parser1
from .forms import PostForm, CommentForm
import requests
from django.views.generic.edit import FormView


def update_news():
    update_buffer = 0
    newrock = parser1.get_news()
    if Post.objects.filter(category=3):
        update_buffer = Post.objects.filter(category=3).earliest('title')
    if newrock[2] not in str(update_buffer):
        update_buffer = newrock[2]
        Post.objects.create(author='РокКульт', title=newrock[2], text=newrock[4],
                            category=get_object_or_404(Category, id=3))
        response = requests.get(newrock[1])
        with open('Metal/static/images/{}.jpg'.format(Post.objects.all()[0].id), 'wb') as f:
            f.write(response.content)


def news(request):
    update_news()
    queryset = Post.objects.all()
    last = queryset[0]
    last_text = last.text[:150]
    featured = queryset.order_by('-post_likes')[0]
    buisness = 0
    top10 = queryset[:10]
    for i in range(len(queryset)):
        if "Бизнес" in repr(queryset[i].category):
            buisness = queryset[i]
    crt = (int(last.id) + 1)
    last_bg_img = '../static/images/{}.jpg'.format(last.id)
    context = {
        'crt': crt,
        'queryset': queryset,
        'last_post': last,
        'last_text': last_text,
        'last_bg_img': last_bg_img,
        'featured': featured,
        'buisness': buisness
    }
    return render(request, 'news.html', context)


def post_delete(request, id=None):
    if get_user(request).user_permissions:
        cookeach = get_object_or_404(Post, id=id).delete()
    return redirect('news')


def post_create(request, id=None):
    if len(request.user.get_group_permissions()) != 0:
        form = PostForm()
        if request.method == 'POST':
            author = get_user(request).username
            title = request.POST.get('title')
            text = request.POST.get('text')
            category = get_object_or_404(Category, id=request.POST.get('category'))
            Post.objects.create(author=author, title=title, text=text, category=category)

        context = {
            'form': form
        }
        return render(request, 'create_post.html', context)
    else:
        return redirect('news')


def post(request, id=None):
    cookeach = get_object_or_404(Post, id=id)
    coms = Comments.objects.order_by('data').filter(comment_post=id)
    form = CommentForm()
    if request.method == 'POST':
        author = get_user(request).username
        text = request.POST.get('comment_text')
        Comments.objects.create(comment_text=text, comment_post=cookeach, comment_author=author)
    context = {
        'comments': coms,
        'comment_form': form,
        'post': cookeach
    }
    return render(request, 'post.html', context)


def hello(request):
    if request.user.is_authenticated:
        return redirect('news/')
    else:
        return render(request, 'hello.html')


def news_by_category(request, id=None):
    catnews = Post.objects.order_by('-data').filter(category=id)
    context = {
        'list': catnews
    }
    return render(request, 'news_by_category.html', context)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login"
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
