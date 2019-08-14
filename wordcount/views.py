from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    #anytime someone come looking for request is accepted by this request object of Home
    return render(request,'home.html')
    #request  name of html file we are trying to send people to

def laddu(request):
    return HttpResponse('laddu are great!')

def count(request):
    fulltext=request.GET['fulltext']

    wordlist=fulltext.split()
    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word]+=1
        else:
            #add o worddictionary
            worddictionary[word]=1

    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
