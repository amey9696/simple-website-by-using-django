#this py file created by me
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("<h1>this is home page<h1>")
#
# def about(request):
#     return HttpResponse("this is about page")

def index(request):
     #para={'name':'amey','city':'guhagar'}
     return render(request,'index.html') #,para)

def analyze(request):
     #get value here
     djtext=request.GET.get('text', 'default')

     #checkbox
     removepunc = request.GET.get('removepunc', 'off')
     fullcaps = request.GET.get('fullcaps', 'off')
     newlineremover = request.GET.get('newlineremover', 'off')
     spaceremover = request.GET.get('spaceremover', 'off')
     # charcount = request.GET.get('charcount', 'off')

     #perform Remove Puncuation Operation
     if removepunc=="on":
          Punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          analyzed = ""
          for char in djtext:
               if char not in Punctuations:
                    analyzed=analyzed+char
          params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
          djtext=analyzed
          #return render(request,'analyze.html',params)
          #return HttpResponse('''<div>remove punc<br><a href="http://127.0.0.1:8000">back</a></div>''')

     # perform UPPERCASE Operation
     if (fullcaps=="on"):
          analyzed = ""
          for char in djtext:
               analyzed=analyzed+char.upper()
          params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
          djtext = analyzed
          # return render(request, 'analyze.html', params)

     if (newlineremover=="on"):
          analyzed = ""
          for char in djtext:
               if char !="\n" and char!="\r":
                    analyzed = analyzed + char
          params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
          djtext = analyzed
          # return render(request, 'analyze.html', params)

     if(spaceremover=="on"):
          analyzed = ""
          for index,char in enumerate(djtext):
               if not (djtext[index]==" " and djtext[index+1]==" "):
                    analyzed = analyzed + char
          params = {'purpose': 'Remove Space', 'analyzed_text': analyzed}
          djtext = analyzed

     if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and spaceremover!="on"):
          return HttpResponse("please select atleast one option..")
     return render(request, 'analyze.html', params)


     # else:
     #      return HttpResponse("Error")









































# def exercise1(request):
#       return HttpResponse('''<div>
#       <h1>Some Important Links</h1><br>
#       <ul>
#            <li><a href='https://github.com/amey9696'>Github</a><br><br></li>
#            <li><a href='https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww'>Code with Harry Youtube Channel</a><br><br></li>
#            <li><a href='https://www.boardinfinity.com/learner/dashboard'>Board Infinity</a><br><br></li>
#            <li><a href='https://www.google.co.in/'>Google</a><br><br></li>
#            <li><a href='https://www.facebook.com/'>Facebook</a><br></li>
#       </ul>
#       </div>''')
#this below function use after some time
# def capfirst(request):
#      return HttpResponse('''<div>capitalized first<br><a href="http://127.0.0.1:8000">back</a></div>''')
#
# def newlineremove(request):
#      return HttpResponse('''<div>new line remove<br><a href="http://127.0.0.1:8000">back</a></div>''')
#
# def charcount(request):
#      return HttpResponse('''<div>char count<br><a href="http://127.0.0.1:8000">back</a></div>''')
#
# def spaceremove(request):
#      return HttpResponse('''<div>space remove<br><a href="http://127.0.0.1:8000">back</a></div>''')