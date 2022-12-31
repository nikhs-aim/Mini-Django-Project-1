from django.http import HttpResponse
from django.shortcuts import render
def had(request):
    return render(request,'had.html')


#punctuation
def punctuation(request):
    return render(request,'punctuation.html')         #this performs functions in newline page
def removepunc(request):
    dj=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(dj)
    print(removepunc)
    punctuations='''()[]{}:;'".,/\\<>-+=!@#$%^&*?~'''
    yourtext=dj
    analyzed=''
    if removepunc=='on':
        for i in dj:
           if i not in punctuations:
              analyzed+=i
        q={'purpose':'Removal of punctuations','analyzed_text':analyzed,'your':yourtext}
        return render (request,'removepunc.html',q)
    else:
        return HttpResponse('Tick the checkbox and try again <br><br><button><a href="/punctuation">Back</a></button>')


#space
def space(request):
    return render(request,'space.html')
def removespace(request):
    sp=request.GET.get('text1', 'default')
    removespace=request.GET.get('space removal', 'off')
    print(sp)
    print(removespace)
    yourtext=sp
    analyzed=''
    if removespace=='on':
        for i in sp:
            if i !=' ':
                analyzed+=i
        s={'purpose':'Removal of space','analyzed_text':analyzed,'your':yourtext}
        return render (request,'removespace.html',s)
    else:
        return HttpResponse('Tick the checkbox and try again <br><br><button><a href="/space">Back</a></button>')


#charactercount
def charactercount(request):
    return render(request,'charactercount.html')
def countcharacter(request):
    cc=request.GET.get('text2','default')
    countchar=request.GET.get('Count character','off')
    print(cc)
    print(countchar)
    analyzed=''
    count=0
    if countchar=='on':
        for i in cc:
            count+=1
            analyzed+=i
        q = {'purpose': 'Character count', 'analyzed_text': analyzed,'char_count':count}
        return render(request, 'countcharacter.html',q)
    else:
        return HttpResponse('Tick the checkbox and try again <br><br><button><a href="/charactercount">Back</a></button>')


#capitalize
def capitalize(request):
    return render(request,'capitalize.html')
def charcapitalize(request):
    ca=request.GET.get('text3','default')
    capitalize=request.GET.get('capitalize','off')
    print(ca)
    print(capitalize)
    yourtext=ca
    analyzed=''
    if capitalize=='on':
        for i in ca:
            c=i.upper()
            analyzed+=c
        r={'purpose':'Capitalize characters','analyzed_text':analyzed,'your':yourtext}
        return render(request,'Charcapitalize.html',r)
    else:
        return HttpResponse('Tick the box and try again <br><br><button><a href="/capitalize">Back</a></button>')