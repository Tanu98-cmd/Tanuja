from django.shortcuts import render,redirect,HttpResponse
import xml.etree.ElementTree as ET
from PIL import Image,ImageFont,ImageDraw
from .forms import *
from django.conf import settings
from .serializers import *
from rest_framework.renderers import JSONRenderer
import datetime
import json
import pandas as pd 
import csv
# Create your vies here.
def home(request):
    imgd='outside'
    form=Fileform()
    if request.method=='GET':
        imgd='inside'
    if request.method == 'POST':
        form=Fileform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            data=Files.objects.all()
            for i in data:
                imgp=i.img
                xmlp=i.xml
            imgp='media/'+str(imgp)
            xmlp='media/'+str(xmlp)
            mytree=ET.parse(xmlp)
            myroot=mytree.getroot()
            pn=myroot[1].text
            image=Image.open(imgp)
            draw=ImageDraw.Draw(image)
            ft=ImageFont.truetype('arial.ttf',30)
            for i in myroot.findall('object'):
                tn=i.find('name').text
                a=int(i.find('bndbox')[0].text)
                b=int(i.find('bndbox')[1].text)
                c=int(i.find('bndbox')[2].text)
                d=int(i.find('bndbox')[3].text)
                idata=imagedata.objects.create(pic_name=pn,obj_name=tn,xmin=a,ymin=b,xmax=c,ymax=d)
                idata.save()
                draw.text(xy=(a,b-30),text=tn,fill='red',font=ft)
                draw.rectangle((a,b,c,d),outline='red',width=3)
            image.save(imgp)
            
    context={'form':form,'imgd':imgd}
    return render(request,'home.html',context)

def filedata(request):
    for i in Files.objects.all():
        d1=i
    serializer=FileSerializer(d1)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
def report(request): 
    sd=request.POST.get('start_date')
    ed=request.POST.get('end_date')
    response=HttpResponse(content_type="tex/csv")
    d2=imagedata.objects.filter(ts__gte=sd).filter(ts__lte=ed)
    writer=csv.writer(response)
    writer.writerow(['picture name','object name','xmin','ymin','xmax','ymax','timestamp'])
    for d in d2.values_list('pic_name','obj_name','xmin','ymin','xmax','ymax','ts'):
        writer.writerow(d)
    response['Content-Disposition']='attachment; filename ="reportextract.csv"'
    return response




