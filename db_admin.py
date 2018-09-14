from blog.models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.db.models import Count


def get_all_posts():
    posts = Post.objects.all().order_by('-pub_date')
    return posts


def posts_paginator(posts_list,page,size):
    paginator = Paginator(list(posts_list), size)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts


def get_featured_posts(limit):
    posts = Post.objects.filter(tag__name="featured").order_by('-pub_date')[:limit]
    return posts


def get_popular_posts(limit):
    posts = Post.objects.order_by('-views')[:limit]
    return posts


def get_recent_posts(limit):
    posts = Post.objects.order_by('-pub_date')[:limit]
    return posts


def get_posts_by_tag(tag_name):
    posts = Post.objects.filter(tag__name=tag_name).order_by('-pub_date')
    return posts


def get_posts_by_author(author_name,limit):
    posts = Post.objects.filter(author__name=author_name).order_by('-pub_date')[:limit]
    return posts


def get_single_post(id):
    post = get_object_or_404(Post,id=id)
    post.body  = post.body.replace('{image1}',post.image_1.url).replace('{image2}',post.image_2.url).replace('{image3}',post.image_3.url).replace('{image4}',post.image_4.url).replace('{image5}',post.image_5.url)
    previous_post =False
    next_post = False
    if Post.objects.filter(id=id - 1).exists():
        previous_post = Post.objects.get(id=id - 1)
    if Post.objects.filter(id=id + 1).exists():
        next_post = Post.objects.get(id=id + 1)
    related = Post.objects.filter(category=post.category).order_by('-pub_date').exclude(id=id)[:3]
    post_tags = post.tag.all()
    return {'related_posts':related,'post': post, 'previous_post': previous_post, 'next_post': next_post,'post_tags':post_tags}


def get_posts_by_category(category, limit):
    posts = Post.objects.filter(category=category).order_by('-pub_date')[:limit]
    return posts


def get_tags():
    tags = Tag.objects.all().annotate(count=Count('name')).order_by('-count')[:11]
    return tags


#useless for now
def get_category_count():
    fashion_count = Post.objects.filter(category='fashion-and-style').count()
    home_count = Post.objects.filter(category='home-and-living').count()
    tech_count = Post.objects.filter(category='technology').count()
    return {'technology': tech_count, 'home': home_count, 'fashion': fashion_count}


def search_posts(query):
    posts = Post.objects.filter(title__icontains=query).order_by('-pub_date')
    return posts


def add_post_view(id_num):
    p = get_object_or_404(Post,id=id_num)
    p.views += 1
    p.save()
    return True



def general_context():
    #category_count = get_category_count()
    tags = get_tags()
    authors = Author.objects.all()
    side_images = get_images()
    fb_count = 856
    ig_count = 1352
    twitter_count = 431
    popular_posts = get_popular_posts(5)
    return {'side_images':side_images,'authors':authors,'tags':tags,'popular_posts':popular_posts,'fb_count':fb_count,'ig_count':ig_count,'twitter_count':twitter_count}


def get_author(name):
    author = get_object_or_404(Author,name=name)
    return author


def get_index_posts():
    recent_posts = get_recent_posts(4)
    featured = get_featured_posts(3)
    main_post = featured[0]
    featured_posts = featured[1:]
    tech_posts = get_posts_by_category('tech-and-gadgets', 3)
    home_posts = get_posts_by_category('home-and-living', 3)
    fashion_posts = get_posts_by_category('fashion-and-style', 3)
    return {'main_post':main_post,'recent_posts':recent_posts,'featured_posts':featured_posts,'tech_posts':tech_posts,'home_posts':home_posts,'fashion_posts':fashion_posts}



def save_mail(email):
    if Subscribers.objects.filter(email__iexact=email).exists():
        return False
    else:
        new_mail = Subscribers(email=email)
        new_mail.save()
        return True

def get_images():
    posts = Post.objects.all().order_by('title')[:6]
    img_list = []
    for post in posts:
        img_list.append({'url':post.image_1.url,'id':post.id})
    return img_list
