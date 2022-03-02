from matplotlib.style import context
import pandas as pd
from pickle import load
import pickle
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from googletrans import Translator

file = open("./ml_model/crs.pkl","rb")
pipe = pickle.load(file)
file.close()

def home(request):
    return render(request, 'home.html')
    #return HttpResponse("this is home page")



def registpage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registpage')
    else:
        form = UserCreationForm()

    return render(request, 'registpage.html',{'form':form})
 
    
def inputpage(request):
        
    return render(request,"input.html")
    #return HttpResponse("this is input page")

def outputpage(request):
    if request.method == "POST":
        N = request.POST.get('N')
        P = request.POST.get('P')
        K = request.POST.get('K')
        temperature= request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        ph = request.POST.get('ph')
        rainfall = request.POST.get('rainfall')
        
    df = pd.DataFrame([[N,P,K,temperature,humidity,ph,rainfall]],columns=["N","P","K","temperature","humidity","ph","rainfall"])
    pred = pipe.predict(df)
    x = pred[0]
    # print(x)
    trans =Translator()
    hindi = trans.translate(x,dest='hindi')
    # print(hindi.text)
    context = {
        'x':x,
        'hindi':hindi.text
    }
    return render(request,'output.html',context)
    #return HttpResponse("this is output page")