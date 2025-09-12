from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse

class BlogSiteMap(Sitemap):
    priority = '0.5'
    changefreq = 'weekly'

    def items(self):
        return Post.objects.filter(status=1)
    
    def lastmod(self,obj):
        return obj.published
    
    def location(self, item):
        return reverse('myblog:blog_single', kwargs={'pid':item.id})

