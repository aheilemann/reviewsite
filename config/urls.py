from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from reviewsite.reviews import views

# create router for backend api
apiRouter = routers.DefaultRouter()
apiRouter.register(r"reviews", views.ReviewViewSet)
apiRouter.register(r"categories", views.CategoryViewSet)
apiRouter.register(r"users", views.UserViewSet)

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("reviewsite.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("reviews/", include("reviewsite.reviews.urls", namespace="reviews")),
    path("api/", include(apiRouter.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
    path("api/currentuser", views.CurrentUserView.as_view()),
    path('api/token/obtain/', TokenObtainPairView.as_view(), name='token_create'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/current/', views.get_current_user),
    path('api/user/create/', views.CreateUserView.as_view(), name="create_user"),
    path('api/hello/', views.HelloWorldView.as_view(), name='hello_world'),
    path('api/blacklist/', views.LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
