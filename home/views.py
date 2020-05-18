from django.http import HttpResponse 
from django.shortcuts import render, redirect
import os
from home import forms
from django.views.generic import TemplateView
import os

class Index(TemplateView):
    template_name = 'home/index.html'

def ShipDetection_view(request):
    if request.method == 'POST': 
        form = forms.ShipForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            scale = request.POST.get("scale")
            return predict(request, scale)
    else:
        print(os.getcwd())
        os.system('rm -r ./media/images/')
        form = forms.ShipForm() 
    return render(request, 'home/im.html', {'form' : form}) 

  
def predict(request, scale): 
    path = os.getcwd()

    ls = os.listdir('./media/images/')
    os.chdir(path + '/home/model/SIH5/model/darknet/')
    os.system('python3 r3unfile.py ' + path + '/media/images/' + str(ls[0] + ' ' + path) + ' ' + str(scale))
    os.chdir(path + '/')
    return render(request, 'home/display_images.html')


def Upload(request):
    image = request.POST.get('image')
    print(type(image))
    return render(request, 'home/upload_image.html')

def display_ship_images(request): 
  
    if request.method == 'GET': 
        return render(request, 'home/display_images.html')
