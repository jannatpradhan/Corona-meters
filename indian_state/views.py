import json
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
import requests

"""
req = requests.get('https://api.covid19india.org/data.json')
data1 = req.json()
s = data1['statewise']



req2 = requests.get('https://api.covid19india.org/v2/state_district_wise.json')
data2 = req2.json()
actualdata=[]
for item in s:
    code=item['statecode']

    for o in data2:
        if o['statecode']==code:
            item.update({'district':o['districtData']})
            actualdata.append(item)
for item in actualdata:
    print(item)
"""




# Create your views here.
def home(request):
    
    total=requests.get('https://api.covid19api.com/summary')
    s=total.text
    data=json.loads(s)
    Total=data['Global']['TotalConfirmed']
    new_case=data['Global']['NewConfirmed']
    Total_death=data['Global']['TotalDeaths']

    req = requests.get('https://api.covid19india.org/data.json')
    data1 = req.json()
    s=data1['statewise']
    req2 = requests.get('https://api.covid19india.org/v2/state_district_wise.json')
    data2 = req2.json()
    actualdata = []
    for item in s:
        code = item['statecode']

        for o in data2:
            if o['statecode'] == code:
                item.update({'district': o['districtData']})
                actualdata.append(item)


    return render(request,'index.html',{'s':actualdata,'Total':Total,'new_case':new_case,'Total_death':Total_death})

def check_symptom(request):
    return render(request,'check_symptom.html')

def login(request):
    return render(request,'base.html')


