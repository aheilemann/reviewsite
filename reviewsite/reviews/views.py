from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django_filters import FilterSet
from django_filters.filters import CharFilter
from django_filters.views import FilterView
# from django.http import response
from django_tables2 import SingleTableMixin
from rest_framework import mixins, permissions, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from vote.views import VoteMixin
from rest_framework_simplejwt.tokens import RefreshToken

from ..users.models import User
from .models import Category, Review
from .serializers import (ReviewSerializer, CategorySerializer, UserSerializer,
                          UserSerializerWithToken, GetFullUserSerializer,
                          CustomUserSerializer)
from .tables import ReviewTable


class ReviewFilter(FilterSet):
    title = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Review
        fields = ["category", "title"]


class ReviewListView(SingleTableMixin, FilterView):
    table_class = ReviewTable
    model = Review
    template_name = "reviews/review_list.html"

    filterset_class = ReviewFilter


class ReviewDetailView(DetailView):
    model = Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = [
        "title",
        "category",
        "description",
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = [
        "title",
        "category",
        "description",
    ]
    action = "Update"


class ReviewViewSet(VoteMixin, ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """

    queryset = Review.objects.all().order_by('-hotscore')
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CategoryViewSet(ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CurrentUserView(APIView):
    """
    API endpoint that allows getting current loggedIn user.
    """

    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    API endpoint that allows getting /api/users/current & users to be viewed by logginIn users.
    """

    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.kwargs.get("pk")

        if pk == "current":
            return self.request.user

        return super(UserViewSet, self).get_object()

@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HelloWorldView(APIView):

    def get(self, request):
        return Response(data={"hello":"You are logged in!"}, status=status.HTTP_200_OK)


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)