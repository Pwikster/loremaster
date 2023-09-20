"""
URL paths take this route to gain access to a page
settings -> 
\loremaster_project urls.py -> 
loremaster_app urls.py -> 
loremaster_app views.py -> 
specified function for that view
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls"))
]