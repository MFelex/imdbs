from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .views import movies_list, movies_detail
from .models import Movie, Genre


class MovieListTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Ali', email='Ali@gmail.com', password='123456')
        self.genre = Genre.objects.create(title='Action')
        self.movie = Movie.objects.create(title='Fight Club', release_date='1999-1-1', genre=self.genre, user=self.user)
        url = reverse('movie-list')
        self.response = self.client.get(url)

    def test_status_code_200(self):
        self.assertEquals(self.response.status_code, 200)

    def test_resolve(self):
        my_rout = resolve('/movies/')
        self.assertEquals(my_rout.func, movies_list)

    def test_home_view_contains_link(self):
        movie_url_detail = reverse('movie-detail', kwargs={'movie_id': self.movie.pk})
        self.assertContains(self.response, 'href="{0}"'.format(movie_url_detail))


class MovieDetailTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Ali', email='Ali@gmail.com', password='123456')
        self.genre = Genre.objects.create(title='Action')
        self.movie = Movie.objects.create(title='Fight Club', release_date='1999-1-1', genre=self.genre, user=self.user)
        url = reverse('movie-detail', kwargs={'movie_id': 1})
        self.response = self.client.get(url)

    def test_status_code_200(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_not_found_status_code_404(self):
        url = reverse('movie-detail', kwargs={'movie_id': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)


    def test_resolve(self):
        my_rout = resolve('/movies/1/')
        self.assertEquals(my_rout.func, movies_detail)

    def test_url_back_in_movie_list(self):
        movie_detail = reverse('movie-detail', kwargs={'movie_id': 1})
        response_movie = self.client.get(movie_detail)
        in_home_page = reverse('movie-list')
        self.assertContains(response_movie, 'href="{}"'.format(in_home_page))


    def test_csrf(self):
        url = reverse('movie-detail', kwargs={'movie_id': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')