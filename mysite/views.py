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
       djtext=request.POST.get('text', 'Default')
       print(djtext)
       
       # Check checkbox values
       removepunc = request.POST.get('removepunc', 'off')
       fullcaps = request.POST.get('fullcaps', 'off')
       newlineremover = request.POST.get('newlineremover', 'off')
       exrtaspaceremover = request.POST.get('exrtaspaceremover','off')
       # charcounter = request.POST.get('charcounter','off')
       
       #routing according to checkbox values
       if removepunc== "on":
              punctuations = '''/[-[\]{}()*+?.,\';>\^$|#\:]/,"\\$&"'''
              analyzed=""
              for char in djtext:
                     if char not in punctuations:
                            analyzed = analyzed +char
              params = {'purpose':'remove punctuations','analyzed_text':analyzed}
              djtext= analyzed
              # return render(request, 'analyze.html',params)
       if(fullcaps=='on'):
              analyzed=""
              for char in djtext:
                     analyzed = analyzed + char.upper()       
              params = {'purpose':"Change to upper case",'analyzed_text':analyzed}
              djtext=analyzed
              # return render(request, 'analyze.html',params)
       if(newlineremover=='on'):
              analyzed=" "
              for char in djtext:
                     if char !="\n" and char!='\r':
                            analyzed = analyzed + char
              params={'purpose':'Removed Newlines', 'analyzed_text':analyzed}
              djtext=analyzed
              # return render(request, 'analyze.html', params)
       if(exrtaspaceremover=='on'):
              analyzed=""
              for index, char in enumerate(djtext):
                     if djtext[index]==" " and djtext[index+1]==" ":
                            pass
                     else:
                            analyzed = analyzed + char
              params={'purpose':'Remove Extra Spaces', 'analyzed_text':analyzed}
              djtext = analyzed
              # return render(request, 'analyze.html',params)
       # if charcounter=="on":
       #        analyzed=""
       #        for i in djtext:
       #               i=i+1
              
       #        analyzed =i
       #        params = {'purpose':'Count the Text ', 'analyzed_text':analyzed}
       #        djtext= analyzed
       #        # return render (equest, 'analyze.html',params)    
       if  (removepunc != "on"  and newlineremover!="on" and fullcaps!="on" and exrtaspaceremover!="on"):
              return HttpResponse("Please Go back and use one of the switches to enable text processing")
       else:
              return render (request, 'analyze.html',params)
                            
         
       
def capfirst(request):
       return HttpResponse('''<a href ="/">Back</a><br> Capitalize first''')

def newlinerremove(request):
       return HttpResponse('''<a href ="/">Back</a><br> line remover''')

def spaceremove(request):
       return HttpResponse('''<a href ="/">Back</a><br> space remover''')

def charcount(request):
       return HttpResponse('''<a href ="/">Back</a> character counter''')

       