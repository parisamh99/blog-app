from django import template
from myblog.models import Post, Category
register = template.Library()

@register.simple_tag
def function(name='totalpost'):
    post = Post.objects.filter(status=1).count()
    return post


@register.simple_tag
def posts(name='totalpost'):
    post = Post.objects.filter(status=1)
    return post

@register.filter
def snippet(val, args):
    return val[:args] + "..."

@register.inclusion_tag('myblog/blog-popular.html')
def popular_posts():
    posts = Post.objects.filter(status=1).order_by('published')[:3]
    return {"posts" : posts}

@register.inclusion_tag('myblog/blog-category.html')
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categoreis":cat_dict}
    
    