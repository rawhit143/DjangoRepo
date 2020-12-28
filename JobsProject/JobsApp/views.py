from django.shortcuts import render
from JobsApp.models import *

# Create your views here.
def home(request):
    return render(request,'JobsApp/home.html')
def indore(request):
    rec_list=IndoreJobs.objects.all
    my_dict={'records':rec_list}
    return render(request,'JobsApp/indore_job.html',context=my_dict)
