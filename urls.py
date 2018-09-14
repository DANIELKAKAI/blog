from django.conf.urls import url
from django.urls import path
from blog.views import *


urlpatterns = [
    url(r'^$',index_view,name="index"),
    url(r'^all-posts/',allposts_view,name="allposts"),
    path('category/<str:category>/',category_view,name="categories"),
    path('author/<str:name>/',author_view,name="authors"),
    url(r'^post/(?P<id>\d+)/',post_view,name="posts"),
    url(r'^contacts/$',contacts_view,name="contacts"),
    url(r'^about/$',about_view,name="authors"),
    url(r'^add-posts/',add_posts,name="add-posts"),
    url(r'^subscribe/',subscribe_view,name="subscribe")
]