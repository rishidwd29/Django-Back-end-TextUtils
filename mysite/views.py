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
       
       
def  analyze(request):
       #Get Text from User
       djtext=request.GET.get('text', 'Default')
       
       # Check checkbox values
       removepunc = request.GET.get('removepunc', 'off')
       fullcaps = request.GET.get('fullcaps', 'off')
       newlineremover = request.GET.get('newlineremover', 'off')
       exrtaspaceremover = request.GET.get('exrtaspaceremover','off')
       charcounter = request.GET.get('charcounter','off')
       
       #routing according to checkbox values
       if removepunc== "on":
              punctuations = '''/[-[\]{}()*+?.,\';>\^$|#\:]/,"\\$&"'''
              analyzed=""
              for char in djtext:
                     if char not in punctuations:
                            analyzed = analyzed +char
              params = {'purpose':'remove punctuations','analyzed_text':analyzed}
              return render(request, 'analyze.html',params)
       elif(newlineremover=='on'):
              analyzed=""
              for char in djtext:
                     if char !="\n":
                            analyzed = analyzed + char
              params={'purpose':'Remved Newlines', 'analyzed_text':analyzed}
              return render(request, 'analyze.html', params)
       elif(exrtaspaceremover=='on'):
              analyzed=""
              for index, char in enumerate(djtext):
                     if djtext[index]==" " and djtext[index+1]==" ":
                            pass
                     else:
                            analyzed = analyzed + char
              params={'purpose':'Remove Extra Spaces', 'analyzed_text':analyzed}
              return render(request, 'analyze.html',params)
       elif charcounter=="on":
              analyzed=""
              for i in djtext:
                     i=i+1
              
              analyzed =i
              params = {'purpose':'Count the Text ', 'analyzed_text':analyzed}
              return render (request, 'analyze.html',params)              
                            
       elif(fullcaps=='on'):
              analyzed=""
              for char in djtext:
                     analyzed = analyzed + char.upper()       
              params = {'purpose':"Capitalize",'analyzed_text':analyzed}
              return render(request, 'analyze.html',params)
       else:
              return HttpResponse("error")  
       
       
def capfirst(request):
       return HttpResponse('''<a href ="/">Back</a><br> Capitalize first''')

def newlinerremove(request):
       return HttpResponse('''<a href ="/">Back</a><br> line remover''')

def spaceremove(request):
       return HttpResponse('''<a href ="/">Back</a><br> space remover''')

def charcount(request):
       return HttpResponse('''<a href ="/">Back</a> character counter''')

       