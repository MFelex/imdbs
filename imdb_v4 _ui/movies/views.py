from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Movie, MovieCrew, MovieComment, MovieRate
from .forms import MovieCommentForm, MovieRateForm


def movies_list(request):
    movie_list = Movie.objects.all().order_by('-release_date')[:10]
    context = {
        'm_list': movie_list,

    }
    return render(request, 'movies/home.html', context)


def movies_detail(request, movie_id, comment_form=None, rate_form=None):
    movie = get_object_or_404(Movie, pk=movie_id)
    if comment_form is None:
        comment_form = MovieCommentForm()
    if rate_form is None:
        rate_form = MovieRateForm()
    context = {
        'movie': movie,
        'mc_list': MovieCrew.objects.select_related('crew', 'role').filter(movie=movie),
        'dir': MovieCrew.objects.select_related('crew', 'role').filter(movie=movie),

        'comment_list': MovieComment.objects.select_related('user').filter(
            movie=movie,
            status=MovieComment.APPROVED
        ).order_by('-created_time'),
        'rate_form': rate_form,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.Html', context)


@login_required()
def movies_comment(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    mcf = MovieCommentForm(request.POST)
    if not mcf.is_valid():
        return movies_detail(request, movie_id, comment_form=mcf)
    obj = MovieComment()
    obj.movie = movie
    obj.user = request.user
    obj.comment_text = mcf.cleaned_data.get('comment_text')
    obj.save()

    return redirect('movie-detail', movie_id=movie_id)


@login_required()
def movies_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    mrf = MovieRateForm(request.POST)
    if not mrf.is_valid():
        return movies_detail(request, movie_id, rate_form=mrf)
    obj = MovieRate()
    obj.movie = movie
    obj.user = request.user
    obj.point = mrf.cleaned_data.get('rate')
    obj.save()
    return redirect('movie-detail', movie_id=movie_id)


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'release_date', 'genre', 'picture']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = ['title', 'release_date', 'genre', 'picture']
    success_url = '/movies/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.user:
            return True
        return False


class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    success_url = '/movies/'

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.user:
            return True
        return False
