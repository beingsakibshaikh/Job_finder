"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.sitemaps.views import sitemap
from jobs.sitemaps import JobSitemap
from jobs.views import robots_txt



sitemaps = {
    'jobs': JobSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
    path('login/', LoginView.as_view(template_name='jobs/login.html', next_page='home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path("robots.txt", robots_txt),


]

