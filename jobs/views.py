from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
    job_items = Job.objects
    return render(request, 'jobs/home.html', {'jobs_items': job_items})
