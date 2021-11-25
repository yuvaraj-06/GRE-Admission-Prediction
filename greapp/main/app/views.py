from django.shortcuts import render
from django.http import HttpResponse
 

import joblib

model=joblib.load('gre.pkl')


# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'yuvi'})
def add(request):
    a=int((request.POST['a']))
    b=int((request.POST['b']))
    c=int((request.POST['c']))
    d=float((request.POST['d']))
    e=float((request.POST['e']))
    f=float((request.POST['f']))
    g=int((request.POST['g']))

    if 260<=a<=340 and 0<=b<=120 and 0<=d<=5 and 0<=e<=5 and 0<=f<=10 and g <= 10:

        print(a,b,c,d,e,f,g)
        out=model.predict([[a,b,c,d,e,f,g]])
        if out==1:
            c="You will get an admission"
        else:
            c="Sorry, You won't get an admission "

        return render(request,'home.html',{'head':'Result:','res':c,'emoji':'&#9989;'})


    return render(request,'home.html',{'res': 'Invalid Inputs !!!'})

    