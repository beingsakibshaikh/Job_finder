from django.shortcuts import render, get_object_or_404
from .models import Job
from django.contrib.auth.decorators import login_required
from .models import Job, Bookmark
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm
from django.contrib.auth import login



def home(request):
    location = request.GET.get('region')    
    job_type = request.GET.get('job_type')
    category = request.GET.get('category')

    jobs = Job.objects.all()

    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if category:
        jobs = jobs.filter(category__icontains=category)

    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/home.html', context)

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})


@login_required
def bookmark_job(request, job_id):
    job = Job.objects.get(id=job_id)
    Bookmark.objects.get_or_create(user=request.user, job=job)
    return redirect('home')  # or 'job_detail', etc.

@login_required
def my_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user).select_related('job')
    return render(request, 'jobs/my_bookmarks.html', {'bookmarks': bookmarks})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log them in after signup
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'jobs/register.html', {'form': form})