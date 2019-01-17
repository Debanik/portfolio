from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def allblogs(request):
    blog_items = Blog.objects
    return render(request, 'blog/allblogs.html',{'blogitems':blog_items})

def details(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_details.html',{'detailblog':detail_blog})
