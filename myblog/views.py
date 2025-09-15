from django.shortcuts import render
from django.shortcuts import render,get_object_or_404 ,HttpResponseRedirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NewspaperForm

def blog_view(request, **kwargs):
   posts = Post.objects.filter(status=1)
   if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
   if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
   if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
             
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
    
    


           