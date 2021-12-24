from typing import Dict
import requests

from .models import Job


ENDPOINT="http://139.177.187.188"

def post_job_request(keyword:str=None) -> Dict:
    result = {}
    r = requests.post(ENDPOINT+'/scraper/'+keyword)
    if r.status_code in range(200,299):
        data_back = r.json()
        # print("return data_back =", data_back)
        result['work_id'] = data_back['task_id']
        result['status'] = 'pending'
    else:
        result['status'] = 'fail'
        result['work_id'] = ''
    # print('i am passed !',r.status_code)
    
    return result

def check_job_status(work_id:str=None) -> Dict:
    result = {}
    r = requests.get(ENDPOINT+'/check/'+work_id)
    if r.status_code in range(200,299):
        data_back = r.json()
        # print("return result =", data_back)
        if isinstance(data_back, dict):
            result['status'] = 'pending'
        else:
            result['status'] = 'success'
            result['data'] = data_back
    else:
        result['status'] = 'fail'
    # print(result['status'])
    # print(result['data'])
    return result

def update_models():
    object_ = Job.objects.filter(job_result='')
    if not object_:
        return
    for obj in object_:
        result = check_job_status(work_id=obj.work_id)
        print('result[status] == ',result['status'])
        if result['status'] == 'success':
           obj.job_result = result['data']
           obj.save()
    return





if __name__=="__main__":
    # post_job_request(keyword='/scraper/game developer')
    check_job_status(work_id="978d137a-5e80-47e6-b2ec-9d3efebe23f4")
