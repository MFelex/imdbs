from django.urls import path

from .views import movies_detail,movies_list,movies_comment,movies_rating ,MovieDeleteView,MovieUpdateView,MovieCreateView

urlpatterns = [
    path('', movies_list, name='movie-list'),
    path('<int:movie_id>/', movies_detail, name='movie-detail'),
    path('<int:movie_id>/post_comment/', movies_comment, name='movie-post-comment'),
    path('<int:movie_id>/post_rating/', movies_rating, name='movie-post-rating'),
    path('new/', MovieCreateView.as_view(), name='new-movie'),
    path('<int:pk>/update/', MovieUpdateView.as_view(), name='update-movie'),
    path('<int:pk>/delete/', MovieDeleteView.as_view(), name='delete-movie'),

]
