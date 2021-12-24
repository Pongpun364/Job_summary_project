import json
from collections import Counter
import pprint
from django.db import models
from typing import Dict, List



def parse_exp(dummy:models.TextField):
    if dummy == '':
        return [],[],[]
    try:
        d_json = json.loads(json.loads(dummy))
    except:
        d_json = json.loads(dummy)

    min_exp = Counter(d_json['min_exp'].values())
    min_exp.pop('', None)
    max_exp = Counter(d_json['max_exp'].values())
    max_exp.pop('', None)
    labels = list(set(list(min_exp.keys()) + list(max_exp.keys())))
    for label in labels:
        if label not in min_exp.keys():
            min_exp[label] = 0
        if label not in max_exp.keys():
            max_exp[label] = 0
    max_exp = max_exp.items()
    min_exp = min_exp.items()
    max_exp = sorted(max_exp, key= lambda x: int(x[0]))
    min_exp = sorted(min_exp, key= lambda x: int(x[0]))
    max_exp = [x[1] for x in max_exp]
    min_exp = [x[1] for x in min_exp]
    labels = sorted(labels, key= lambda x: int(x))
    return labels, min_exp, max_exp

def parse_skill(dummy:models.TextField):
    if dummy == '':
        return [],[]
    try:
        d_json = json.loads(json.loads(dummy))
    except:
        d_json = json.loads(dummy)
    dict_skill = [json.loads(dt) for dt in d_json['extracted_skill'].values()]
    data = []
    for dt in dict_skill:
        data += [*dt.keys()]
    final = Counter(data)
    # print(final.items())
    data = sorted(final.items(), key=lambda x: x[1] , reverse=True )
    labels = [x[0] for x in data]
    data = [x[1] for x in data]
    return labels, data

def parse_salary(dummy:models.TextField):
    if dummy == '':
        return [],[],[]
    try:
        d_json = json.loads(json.loads(dummy))
    except:
        d_json = json.loads(dummy)
    maxsal = d_json['max_salary'].values()
    minsal = d_json['min_salary'].values()
    maxsal = [ x for x in maxsal if x != '']
    minsal = [ x for x in minsal if x != '']
    max_hist = {}
    min_hist = {}
    for i in maxsal:
        max_hist[i] = max_hist.get(i, 0) + 1
    for i in minsal:
        min_hist[i] = min_hist.get(i, 0) + 1
    min_hist = list(min_hist.items())
    max_hist = list(max_hist.items())
    m_bin = 5000
    new_max_hist = []
    new_min_hist = []
    labels = list(range(8000,150000,m_bin))

    for i in labels:
        max_value = 0
        interval = list(range(i,i+m_bin))
        for j in max_hist:
            if int(j[0]) in interval:
                max_value += j[1]
        new_max_hist.append(max_value)
        
        min_value = 0
        for j in min_hist:
            if int(j[0]) in interval:
                min_value += j[1]
        new_min_hist.append(min_value)

    final_labels = []
    for i,x in enumerate(labels):
        if i == len(labels) - 1:
            final_labels.append('{}k ++'.format(round(x/1000)))
        else:
            final_labels.append('{}k - <{}k'.format(round(x/1000),round(labels[i+1]/1000) ))
    return final_labels, new_min_hist, new_max_hist

def parse_data(obj:models.Model) -> Dict:
    graph_data = {
        "skill": {},
        "exp": {},
        "sal": {}
    }
    dummy = obj.job_result
    graph_data['skill']['labels'], graph_data['skill']['data'] = parse_skill(dummy)
    graph_data['exp']['labels'], graph_data['exp']['min_exp'],graph_data['exp']['max_exp'] = parse_exp(dummy)
    graph_data['sal']['labels'], graph_data['sal']['min_sal'],graph_data['sal']['max_sal'] = parse_salary(dummy)
    return graph_data

