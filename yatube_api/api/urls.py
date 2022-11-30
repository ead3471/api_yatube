from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
