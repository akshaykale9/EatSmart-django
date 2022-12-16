from django.shortcuts import render ,HttpResponse
import pandas as pd
import os
from diet.settings import BASE_DIR
from recommender.functions import Weight_Gain ,Weight_Loss,Healthy
from recommender.models import Food

# Create your views here.
def index(request):
    if request.method=="POST":
        age=int(request.POST.get("age"))
        weight=int(request.POST.get("weight"))
        height=int(request.POST.get("height"))
        bodyfat=float(request.POST.get("bodyfat"))
        goal=request.POST.get("goal")
        activity=float(request.POST.get("activity"))
        gender=request.POST.get("gender")

        leanfactor=0.0
        if(gender=="m"):
            if(10<=bodyfat<=14):
                leanfactor=1
            elif(15<=bodyfat<=20):
                leanfactor=0.95
            elif(21<=bodyfat<=28):
                leanfactor=0.90
            else:
                leanfactor=0.85    
        else:
            if(14<=bodyfat<=18):
                leanfactor=1
            elif(19<=bodyfat<=28):
                leanfactor=0.95
            elif(29<=bodyfat<=38):
                leanfactor=0.90
            else:
                leanfactor=0.85            


        maintaincalories=int(weight*24*leanfactor*activity)
        
        caloriesreq=0
        finaldata=[]
        bmi=0
        bmiinfo=""
        if(goal=="weight gain"):
            print("wg")
            finaldata=Weight_Gain(age,weight,height)
            bmi=int(finaldata[len(finaldata)-2])
            bmiinfo=finaldata[len(finaldata)-1]
            caloriesreq=maintaincalories+300
        if(goal=="weight loss"):
            print("wl")
            finaldata=Weight_Loss(age,weight,height)
            bmi=int(finaldata[len(finaldata)-2])
            bmiinfo=finaldata[len(finaldata)-1]
            caloriesreq=maintaincalories-300
        
        if(goal=="healthy"):
            print("h")
            finaldata=Healthy(age,weight,height)
            bmi=int(finaldata[len(finaldata)-2])
            bmiinfo=finaldata[len(finaldata)-1]
            caloriesreq=maintaincalories
  
        breakfastdata=Food.objects.all().filter(bf=1).filter(name__in=finaldata)
        lunchdata=Food.objects.all().filter(lu=1).filter(name__in=finaldata)
        dinnerdata=Food.objects.all().filter(di=1).filter(name__in=finaldata)

        context={
            "breakfast":breakfastdata,
            "lunch":lunchdata,
            "dinner":dinnerdata,
            "bmi":bmi,
            "bmiinfo":bmiinfo,
            "caloriesreq":caloriesreq
        }

        return render(request,"diet.html",context)
    
    return render(request,"index.html")

def bodymass(request):
    return render(request,"bodymass.html")   

def home(request):
    return render(request,"home.html")        

def login(request):
    return render(request,"login.html")            

def diet(request):
    return render(request,"diet.html")

def about(request):
    return render(request,"about.html")  