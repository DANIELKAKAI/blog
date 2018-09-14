from django.shortcuts import render
from django.http import JsonResponse
from blog.db_admin import *
from django.template.loader import render_to_string


def index_view(request):
    context = get_index_posts()
    context.update(general_context())
    return render(request, "blog/index.html", context)


def allposts_view(request):
    title = "all blogs"
    tag_param = ""
    search_param = ""
    page = request.GET.get('page', 1)
    if request.GET.get('tag', None):
        tag = request.GET.get('tag')
        title = tag
        tag_param = "&tag="+tag
        posts = get_posts_by_tag(str(tag))
    elif request.GET.get('search', None):
        query = request.GET.get('search').strip().lower()
        title = query
        search_param = "&search="+query
        posts = search_posts(str(query))
    else:
        posts = get_all_posts()
    posts = posts_paginator(posts, page, size=16)
    context = {'title': title, 'posts': posts,'tag_param':tag_param,'search_param':search_param}
    context.update(general_context())
    return render(request, "blog/allblogs.html", context)


def category_view(request, category):
    posts = get_posts_by_category(category, limit=None)
    top_post = posts[0]
    box_posts = posts[1:5]
    linear_posts = posts[5:10]
    category = category.replace("-", " ")
    load_button = False
    if len(posts) > 10: load_button = True;
    context = {'title': category, 'top_post': top_post, 'box_posts': box_posts, 'linear_posts': linear_posts,
               'load_button': load_button}
    context.update(general_context())
    return render(request, "blog/category.html", context)


def author_view(request, name):
    posts = get_posts_by_author(name, limit=None)
    author = get_author(str(name))
    load_button = False
    if len(posts) > 10: load_button = True;
    context = {'posts': posts[:10], 'author': author, 'load_button': load_button}
    context.update(general_context())
    return render(request, "blog/author.html", context)


def post_view(request, id):
    post_data = get_single_post(int(id))
    popular_posts = get_popular_posts(5)
    post_url = request.build_absolute_uri()
    context = {'post_url': post_url, 'popular_posts': popular_posts}
    context.update(general_context())
    context.update(post_data)
    response = render(request, "blog/blog-post.html", context)
    if request.COOKIES.get(str(id)) == None:
        add_post_view(int(id))
        response.set_cookie(str(id), True)
    return response


def add_posts(request):
    category = request.GET.get('category', None)
    author = request.GET.get('author', None)
    if request.is_ajax():
        page = int(request.GET.get('page', 2))
        if category:
            posts = get_posts_by_category(category, None)
        if author:
            posts = get_posts_by_author(author, None)
        posts = posts_paginator(posts, page, size=10)
        html = render_to_string("blog/extra_post.html", context={'posts': posts})
        data = {'posts': html, 'next_page': page + 1, 'has_next': posts.has_next()}
        return JsonResponse(data)


def subscribe_view(request):
    if request.is_ajax():
        email = request.POST.get('email')
    if email:
        result = save_mail(email)
        data = {'result': result}
        return JsonResponse(data)


def contacts_view(request):
    context = general_context()
    return render(request, "blog/contact.html", context)


def about_view(request):
    context = general_context()
    return render(request, "blog/about.html", context)
