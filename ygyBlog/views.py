from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.http import JsonResponse

from .models import BlogCategory, Blog, BlogComment
from .forms import PostBlogForm
from django.db.models import Q


def index(request):
    """
    Show the latest 4 posts on the home page.
    """

    blogs = Blog.objects.all().order_by('-post_date')[:4]
    return render(request, 'index.html', {'blogs': blogs})


def blog_tags(request):
    """
    Show all the categories on tags page.
    """

    categories = BlogCategory.objects.all()
    return render(request, 'tags.html', {'categories': categories})


def blog_about(request):
    """
    About page.
    """
    return render(request, 'about.html')


def blog_profile(request, user_id):
    """
    Show user's name and posts on the profile page.
    """

    user = get_object_or_404(User, id=user_id)
    blogs = Blog.objects.filter(author_id=user_id)
    return render(request, 'profile.html', {'user': user, 'blogs': blogs})


def blog_all(request):
    """
    Show all posts on this page.
    """

    blog_list = Blog.objects.all().order_by('-post_date')
    # Show 4 posts on each page
    paginator = Paginator(blog_list, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'all_posts.html', {'page_obj': page_obj})


def blog_detail(request, blog_id):
    """
    Show the content of a post on this page.
    """

    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})


def blog_tag_posts(request, category_id):
    """
    Show all posts with a certain tag on this page.
    """

    category = get_object_or_404(BlogCategory, id=category_id)
    blogs = Blog.objects.filter(category=category)
    return render(request, 'tag_posts.html', {'category': category, 'blogs': blogs})


@require_http_methods(['GET', 'POST'])
@login_required(login_url='/auth/login/')
def post_blog(request):
    """
    Post a blog.
    """

    if request.method == 'GET':
        categories = BlogCategory.objects.all()
        return render(request, 'post_blog.html', {'categories': categories})

    else:
        form = PostBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            blog = Blog.objects.create(title=title, content=content, category_id=category_id, author=request.user)
            return JsonResponse({'code': 200, 'message': 'Blog created!', 'data': {'blog_id': blog.id}})
        else:
            print(form.errors)
            return JsonResponse({'code': 400, 'message': 'Invalid data!'})


@require_POST
@login_required(login_url='/auth/login/')
def post_comment(request):
    """
    Comment.
    """

    blog_id = request.POST.get('blog_id')
    content = request.POST.get('content')
    BlogComment.objects.create(content=content, blog_id=blog_id, author=request.user)
    return redirect(reverse('ygyBlog:blog_detail', kwargs={'blog_id': blog_id}))


@require_GET
def search(request):
    """
    Search.
    """

    # / search?q = xxx
    q = request.GET.get('q')
    blogs = (Blog.objects.filter(
        Q(title__icontains=q) |
        Q(content__icontains=q) |
        Q(category__name__icontains=q) |
        Q(author__username__icontains=q)).all())

    return render(request, 'search_posts.html', {'blogs': blogs})
