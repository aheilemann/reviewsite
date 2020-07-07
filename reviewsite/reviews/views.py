from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Review, Category

class ReviewListView(ListView):
    model = Review
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-category')
        # validate ordering here
        return ordering

class ReviewDetailView(DetailView):
    model = Review

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = [
        'author',
        'title',
        'category',
        'description',
    ]

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = [
        'author',
        'title',
        'category',
        'description',
    ]
    action = 'Update'


class CategoryListView(ListView):
    model = Category
