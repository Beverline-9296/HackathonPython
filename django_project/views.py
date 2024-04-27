from  django.shortcuts import render
import requests

def index(request):
  r1 = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random?language-en')
  res1 = r1.json()  
  fact = res1['text']  

  r2 = requests.get('https://www.boredapi.com/api/activity')
  res2 = r2.json()  
  activity = res2['activity'] 

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()  
  dog = res3['message']
  
  r4 = requests.get('https://api.quotable.io/random')
  res4 = r4.json()  
  truth = res4['content'] 
  author = res4['author']
  
  r5 = requests.get('https://api.thecatapi.com/v1/images/search')
  res5 = r5.json()
  cat = res5[0]['url']
  
  if request.method == 'POST':
    photo=request.POST.get('photo')
  else:
    photo = None
     
  return render(request, 'templates/index.html',{'fact':fact,'activity':activity,'dog':dog,'photo':photo, 'truth':truth ,'author':author ,'cat':cat })
  