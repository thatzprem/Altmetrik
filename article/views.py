from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from article.serializers import UserSerializer,ArticleSerializer
from article.models import Article
from rest_framework import generics, filters
from rest_framework.viewsets import ModelViewSet

def index(request, template_name=None):
#     return HttpResponse("Hello, world. You're at the crawler index.")
    if template_name is None:
        template_name = 'index.html'
        
    return render(request, template_name, None)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer   


class ArticleMixin(object):        
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()   
    filter_backends = (filters.OrderingFilter, )
                 
    
class ArticleViewSet(ArticleMixin, ModelViewSet):
        
    def create(self, request, *args, **kwargs):                       
        return ModelViewSet.create(self, request, *args, **kwargs)
        
    def update(self, request, *args, **kwargs):      
        return ModelViewSet.update(self, request, *args, **kwargs)
        
   



