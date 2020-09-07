from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path(route="", view=views.ReviewListView.as_view(), name="list"),
    path(route="add/", view=views.ReviewCreateView.as_view(), name="add"),
    path(route="<slug:slug>/", view=views.ReviewDetailView.as_view(), name="detail"),
    path(
        route="<slug:slug>/update/",
        view=views.ReviewUpdateView.as_view(),
        name="update",
    ),
]
