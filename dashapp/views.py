from django.shortcuts import render

from django.http import HttpResponse
from django.template.context_processors import request
from .models import Testrun, Release, Product
import json
from django.template import loader

def index(request):
    
    return render(request, 'dashapp/index.html')
    #return HttpResponse("Hello, world. You're at the polls index.")

def release_status(request, release_id):
    status = {}
    for v in ['PASS','FAIL','NOT_TESTED']:
        status[v] = Testrun.objects.filter(release_id=release_id, test_result=v).count()
    
    json_data = json.dumps(status)
    print(json_data)
    return HttpResponse(json_data)

def status_by_release_name(request, release):
    status = {}
    try:
        r = Release.objects.get(release_name__iexact=release)
    except:
        return HttpResponse("release does not exist")
    
    for v in ['PASS','FAIL','NOT_TESTED']:
        status[v] = Testrun.objects.filter(release_id = r.id, test_result=v).count()
    
    json_data = json.dumps(status)
    print(json_data)
    return HttpResponse(json_data)

def piechart_json(request):
    pie = []
    data = {}
    for v in ['PASS','FAIL','NOT_TESTED']:
        p = Testrun.objects.filter(release_id=1, test_result=v).count()
        pie.append(p)
        
    data['datasets'] = [{'data': pie}]
    data['labels'] = ['Pass', 'fail', 'not_tested']
    
    json_data = json.dumps(data)
    print(json_data)
    #return HttpResponse(json_data)
    template = loader.get_template('dashapp/index.html')
    context = {'data': data}
    return HttpResponse(template.render(context, request))

def barchart_json(request):
    release_status = {}
    pie1 = {} 
    pie2 ={} 
    p1  = Testrun.objects.filter(release_id=1, test_result='PASS').count()
    f1  = Testrun.objects.filter( release_id=1, test_result='FAIL').count()
    nr1 = Testrun.objects.filter( release_id=1, test_result='NOT_TESTED').count()
    pie1['pass'] = p1
    pie1['fail'] = f1
    pie1['not_tested'] = nr1
    p2  = Testrun.objects.filter(release_id=2, test_result='PASS').count()
    f2  = Testrun.objects.filter( release_id=2, test_result='FAIL').count()
    nr2 = Testrun.objects.filter( release_id=2, test_result='NOT_TESTED').count()
    pie2['pass'] = p2
    pie2['fail'] = f2
    pie2['not_tested'] = nr2
    release_status ={"ford_1":pie1, "ford_2":pie2}
    json_data = json.dumps(release_status)
    print(json_data)
    return HttpResponse(json_data)

def product_status(request):
    product_status = {}
    for r in ['Ford_1','Maruti_1','BMW_1','Audi_1','Hyundai_1']:
        t = {}
        t['pass']  = Testrun.objects.filter(release_id__release_name=r, test_result='PASS').count()
        t['fail']  = Testrun.objects.filter(release_id__release_name=r, test_result='FAIL').count()
        t['not_tested']  = Testrun.objects.filter(release_id__release_name=r, test_result='NOT_TESTED').count()
        product_status[r]=t
    
    json_data = json.dumps(product_status)
    print(json_data)
    return HttpResponse(json_data)   
    
def get_product_latest_status(request, product_id):
     
    try:
        id = int(product_id)
        product = Product.objects.get(pk=id)
        print(product)
    except:
        return HttpResponse("Product does not exist")
    
    r = Release.objects.filter(product_id=1).order_by('-release_id')[0]
    p = Testrun.objects.filter(release_id=r, test_result='PASS').count()
    f = Testrun.objects.filter(release_id=r, test_result='FAIL').count()
    nt = Testrun.objects.filter(release_id=r, test_result='NOT_TESTED').count()
    data = {'name':product.product_name, 'pass': p, 'fail': f, 'not_test': nt}
    context = {'data' : data}
        
    return render(request, 'dashapp/index.html', context)
    
        
    