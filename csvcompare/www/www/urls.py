from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'diffs', views.DiffViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^diffs/(?P<pk>[0-9]+)/show/$', views.DiffShow.as_view(), name='diff-show'),
    url(r'^backend/', include(admin.site.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
