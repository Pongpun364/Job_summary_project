
from django.shortcuts import render
from .models import Job
from .utils import parse_data
from django.contrib import messages
from .services import post_job_request,update_models
# Create your views here.


def Home(request):
    return render(request, 'search/base.html')

def search_snippet(request):
    snippet = "search/partial/search_result.html"
    query = request.GET.get('q')
    update_models()
    # print('query is ...', query)
    obj = Job.objects.filter(job_search__icontains=query)

    if query=='':
        obj = [None]
        context = {"obj_list": obj}
        return render(request, snippet, context=context)

    if not obj.exists():
        snippet = "search/partial/not_found.html"

    context = {"obj_list": obj}
    return render(request, snippet, context=context)

def graph(request, word=None):
    graph_data = {}
    template = "search/job_graph.html"
    obj = Job.objects.get(job_search=word)
    graph_data = parse_data(obj)
    context = {
        "graph":graph_data,
        "obj": obj
        }
    return render(request, template, context=context)

def request_job(request):
    # print(request.POST)
    query = request.POST.get('query')
    print('query ==', query)
    result = post_job_request(keyword=query)
    if result['status'] == 'pending':
        obj = Job.objects.create(job_search=query,work_id=result['work_id'])
    # print('CREATE SUCCESS', obj.work_id)
    messages.info(request, f"your request for <p class='s-text'>'{query}'</p> is sent to microservice !. please wait....")
    return render(request,'search/partial/message.html')

