from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stream', views.StreamPlateformViewSet, basename='streamplateform')

urlpatterns = [
    path('list/',views.movie_list, name="movie-list" ),
    path("list/<int:pk>/", views.movie_detail, name='movie-detail'),
    path('', include(router.urls)),
    path('', views.api_root),
]





# streamplateform_list = views.StreamPlateformViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
#     })


# streamplateform_detail = views.StreamPlateformViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })

# urlpatterns = [
#     path('list/',views.movie_list, name="watchlist-list" ),
#     path("list/<int:pk>/", views.movie_detail, name='watchlist-detail'),
#     path("stream/", streamplateform_list, name="streamplateform-list"),
#     path("stream/<int:pk>/", streamplateform_detail, name="streamplateform-detail"),
#     path('', views.api_root),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


