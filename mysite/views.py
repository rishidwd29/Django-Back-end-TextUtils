# I have created this file - Rishi
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
       
       return render(request,'index.html')
       
       
def about(request):
       
       return HttpResponse()
              
              
def five_web(request):
       return HttpResponse('''<h1>My Favorite website</h1> <br> 
                           <a href="https://drive.google.com/drive/search?q=owner:me%20(type:application/vnd.google.colaboratory%20||%20type:application/vnd.google.colab)>"
                           <h3>Colaboratory</h3>
                           <a href="https://www.youtube.com/">
                           <h3>Youtube</h3>
                           ''')
def  removepunc(request):
       print(request.GET.get('text', 'Default'))
       return HttpResponse('''<a href ="/">Back</a><br> remove punchuations''')

def capfirst(request):
       return HttpResponse('''<a href ="/">Back</a><br> Capitalize first''')

def newlinerremove(request):
       return HttpResponse('''<a href ="/">Back</a><br> line remover''')

def spaceremove(request):
       return HttpResponse('''<a href ="/">Back</a><br> space remover''')

def charcount(request):
       return HttpResponse('''<a href ="/">Back</a> character counter''')

       