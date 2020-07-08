from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView

# Create your views here.
from .models import Review, Category
from .tables import ReviewTable


class ReviewListView(SingleTableView):
    model = Review
    table_class = ReviewTable


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


class CategoryListView(ListView):
    model = Category
