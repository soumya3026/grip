from django.shortcuts import render
from .models import Customer,Transaction
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'bbs/index.html')

def show(request):
    cusobj=Customer.objects.all()
    return render(request,'bbs/show.html',{"Customer":cusobj})

def detail(request):
    if request.method=="POST":
        sender=request.POST['sender']
        receiver=request.POST['receiver']
        transfer=request.POST['transfer']
        p=Customer.objects.filter(name=sender).exists()
        q=Customer.objects.filter(name=receiver).exists()
        if p and q:
            for i in Customer.objects.all():
                if sender==i.name:
                    for j in Customer.objects.all():
                        if receiver==j.name:
                            if int(transfer)<=i.current_balance:
                                i.current_balance=i.current_balance-int(transfer)
                                j.current_balance=j.current_balance+int(transfer)
                                i.save()
                                j.save()
                                Transaction(sender=sender,receiver=receiver,transfer=transfer).save()
                                messages.success(request,"Rs."+request.POST['transfer']+" has been sent from "+request.POST['sender']+" to "+request.POST['receiver']+" successfully!")
                                messages.info(request,"Current Balance:")
                                messages.info(request,request.POST['sender']+"--Rs."+str(i.current_balance))
                                messages.info(request,request.POST['receiver']+"--Rs."+str(j.current_balance))
                            else:
                                messages.warning(request,"available balance is low!")
    return render(request,'bbs/detail.html')

