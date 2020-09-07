from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from django_filters.filters import CharFilter
from django_filters import FilterSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from vote.views import VoteMixin

# Create your views here.
from .models import Review, Category
from .tables import ReviewTable
from .serializers import ReviewSerializer, CategorySerializer


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
    queryset = Review.objects.all()  # .order_by('-date_joined')
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CategoryViewSet(ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()  # .order_by('-date_joined')
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
