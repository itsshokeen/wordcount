
from django.shortcuts import render
import operator



def homepage(request):
   return render(request,'home.html')

def count(request):
    data=request.GET['fulltextarea']
    word_list=data.split()
    list_length=len(word_list)

    worddectionary={}

    for word in word_list:
        if word in worddectionary:
            worddectionary[word]+=1
        else:
            worddectionary[word]=1

    sorted_list=sorted(worddectionary.items(),key=operator.itemgetter(1))

    return render(request,'count.html',{'fulltext':data,'words':list_length,'worddectionary': sorted_list})

def about(request):
    return render(request,'about.html')