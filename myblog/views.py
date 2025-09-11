from django.shortcuts import render
from django.shortcuts import render,get_object_or_404 ,HttpResponseRedirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NewspaperForm

def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
         posts = posts.filter(category__name = cat_name)
    if author_username:
         posts = posts.filter(author__username = author_username) 
    posts = Paginator(posts,3)
    try: 
      page_number = request.GET.get('page') 
      posts = posts.get_page(page_number)
    except PageNotAnInteger:
      posts = posts.get_page(1)
    except EmptyPage:
      posts = posts.get_page(1)         
    content = {"posts":posts}
    return render (request, 'myblog/blog-home.html', content)



def single_blog_view(request,pid):
     posts = get_object_or_404(Post, pk=pid)
     content = {"posts":posts}
     return render (request, 'myblog/single-blog.html',content)



def test(request):
     return render (request, 'test.html')




def blog_category(request,cat_name):
     posts = Post.objects.filter(status=1)
     posts = posts.filter(category__name=cat_name)
     content = {'posts':posts}
     return render(request,'myblog/blog-home.html', content)


def blog_search(request):
     posts = Post.objects.filter(status=1)
     if request.method=='GET':
          posts = posts.filter(content__contains=request.GET.get('s'))
     content = {'posts':posts}
     return render(request, 'myblog/blog-home.html', content)


def newspaper(request):
    if request.method == 'POST':
        form = NewspaperForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    
    


           