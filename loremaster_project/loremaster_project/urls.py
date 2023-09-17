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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loremaster_app.urls')),
]


