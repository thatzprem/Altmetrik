from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from article.views import UserViewSet, ArticleViewSet
from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'article', ArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^interface/',views.index,name="index"), 
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]