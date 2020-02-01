# i have created this file -- govi
from django.http import HttpResponse
from django.shortcuts import render

def navigationBar(request):
    sites = {'''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             }
    return HttpResponse(sites)

def index(request):
    return render(request , 'index.html')

def about(request):
    return HttpResponse ("Hiii Govinda")

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"/,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if (fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to capatalize', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover=="on"):
        analyzed = " "
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount=="on"):
        analyzed = " "
        for char in djtext:
            analyzed = len(djtext.split())
        params = {'purpose': 'Charecter Counter', 'analyzed_text': analyzed}

    if (removepunc!="on" and extraspaceremover!="on" and fullcaps!="on" and newlineremover!="on" and charcount!="on"):
        return HttpResponse("Please select any opration and try again")
        djtext = analyzed

    return render(request, 'analyze.html', params)
