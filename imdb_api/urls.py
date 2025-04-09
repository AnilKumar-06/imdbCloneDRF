from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('list/',views.movie_list, name="movie-list" ),
    path("list/<int:pk>/", views.movie_detail, name='movie-detail'),
    path("stream/", views.stream_list, name="stream-plateform"),
    path("stream/<int:pk>/", views.stream_detail, name="stream-plateform-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
