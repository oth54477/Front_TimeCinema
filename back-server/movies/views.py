from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.decorators.http import require_safe, require_POST
from .models import Movie, MovieComment, MovieCommentReply
from accounts.models import User

from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from django.core import serializers
from .serializers import MovieListSerializer, MovieSerializer, MovieCommentSerializer, MovieCommentReplySerializer, MovieLikeSerializer, UserAllSerializer, MovieWatchSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import CommentForm

from django.conf import settings

import datetime

# Create your views here.
@require_safe
def index(request):
    # movies = get_list_or_404(Movie)
    movies = Movie.objects.all()
    context = {"movies": movies}
    return render(request, "movies/index.html", context)


@api_view(["GET"])
def movie_list(request):
    movies_list = []
    start_date = datetime.date(2022, 7, 1)
    end_date = datetime.date(2022, 7, 31)
    movies = Movie.objects.filter(release_date__range=(start_date, end_date))
    serializer = MovieListSerializer(movies, many=True)
    movies_list.append(serializer.data)
    start_date = datetime.date(2022, 8, 1)
    end_date = datetime.date(2022, 8, 31)
    movies = Movie.objects.filter(release_date__range=(start_date, end_date))
    serializer = MovieListSerializer(movies, many=True)
    movies_list.append(serializer.data)
    start_date = datetime.date(2022, 9, 1)
    end_date = datetime.date(2022, 9, 30)
    movies = Movie.objects.filter(release_date__range=(start_date, end_date))
    serializer = MovieListSerializer(movies, many=True)
    movies_list.append(serializer.data)
    start_date = datetime.date(2022, 10, 1)
    end_date = datetime.date(2022, 10, 31)
    movies = Movie.objects.filter(release_date__range=(start_date, end_date))
    serializer = MovieListSerializer(movies, many=True)
    movies_list.append(serializer.data)
    return Response(movies_list)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm()
    context = {"movie": movie, "comment_form": comment_form}
    return render(request, "movies/detail.html", context)


@api_view(["GET"])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    # print(serializer['comment_set'].value())
    return Response(serializer.data)



@api_view(["GET"])
def comment_list(request, movie_pk):
    comments = MovieComment.objects.filter(movie=movie_pk)
    print(comments)
    print(request.user.pk, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(User.objects.all())
    serializer = MovieCommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def reply_list(request, movie_pk, comment_pk):
    reply = MovieCommentReply.objects.filter(comment=comment_pk)
    serializer = MovieCommentReplySerializer(reply, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def comment_create(request, movie_pk):
    # print(request.data)
    # article = Article.objects.get(pk=article_pk)
    movie = Movie.objects.get(pk=movie_pk)
    # movie = get_object_or_404(Movie, pk=movie_pk)
    # print(request.data['user'])
    user = User.objects.get(pk=request.user.pk)
    serializer = MovieCommentSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer['user'])



@api_view(["POST"])
def reply_create(request, movie_pk, comment_pk):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(MovieComment, pk=comment_pk)
    user = User.objects.get(pk=request.user.pk)
    serializer = MovieCommentReplySerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(comment=comment, movie=movie, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        best_movie = Movie.objects.all().order_by("-popularity")[0]
        recommended_movies = Movie.objects.all().order_by("-popularity")[1:10]
        context = {"best_movie": best_movie, "movies": recommended_movies}
        return render(request, "movies/recommended.html", context)
    return redirect("accounts:login")


@api_view(["POST"])
def movie_like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            is_like = False
        else:
            movie.like_users.add(user)
            is_like = True
        context = MovieLikeSerializer(movie).data
        context["is_like"] = is_like
        context["like_user_count"] = movie.like_users.count()
    else: 
        context = {}
    return Response(context)


@api_view(["POST"])
def movie_watch(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        if movie.watch_users.filter(pk=user.pk).exists():
            movie.watch_users.remove(user)
            is_watch = False
        else:
            movie.watch_users.add(user)
            is_watch = True
        context = MovieWatchSerializer(movie).data
        context["is_watch"] = is_watch
        context["watch_user_count"] = movie.watch_users.count()
    else: 
        context = {}
    return Response(context)


@api_view(["GET"])
def user_list(request):
    users = User.objects.all()
    serializer = UserAllSerializer(users, many=True)
    return Response(serializer.data)