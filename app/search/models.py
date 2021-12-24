from django.db import models
from django.urls import reverse
# Create your models here.


class Job(models.Model):
    job_search = models.CharField(max_length=50)
    job_result = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    work_id = models.CharField(blank=True,max_length=60)

    def __str__(self):
        return self.job_search

    def get_absolute_url(self):
        return reverse("search:graph-result", kwargs={"word": self.job_search})
    
    


