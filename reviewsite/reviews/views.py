from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from django_filters.filters import CharFilter
from django_filters import FilterSet

# Create your views here.
from .models import Review
from .tables import ReviewTable


class ReviewFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Review
        fields = ['category', 'title']

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
        'title',
        'category',
        'description',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = [
        'title',
        'category',
        'description',
    ]
    action = 'Update'
