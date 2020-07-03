from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Review

class ReviewListView(ListView):
    model = Review

class ReviewDetailView(DetailView):
    model = Review