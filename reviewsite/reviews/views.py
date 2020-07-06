from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Review

class ReviewListView(ListView):
    model = Review

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