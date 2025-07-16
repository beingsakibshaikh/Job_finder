from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('bookmark/<int:job_id>/', views.bookmark_job, name='bookmark_job'),
    path('bookmarks/', views.my_bookmarks, name='my_bookmarks'),
    path('register/', views.register, name='register'),

]
