from django.shortcuts import render, HttpResponse
from .models import Apply
import urllib.parse #.quote
import webbrowser

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
    
def apply(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        idea = request.POST.get('idea')
        budget = request.POST.get('budget')
        #save to db
        try:
            Apply.objects.create(
                name = name,
                tel = tel,
                email = email,
                idea = idea,
                budget = budget
            )
            
            message = f"Name: {name}\nPhone: {tel}\nEmail: {email}\n\nMy Idea is \n{idea}.\n\n I have a budget of {budget}"
            enc_msg= urllib.parse.quote(message)
            url=f"https://wa.me/256706749801?text={enc_msg}"
            print('\n\n==>Encoded message well\n\n')
            if webbrowser.open(url):
                return  HttpResponse('<h1>Submitted successfully! We gonna contact you very soon and discuss the rest. Thank you <br/> <a href="/"> Click here to go back</a>')
            
           # print('\n\n==>Sent message well\n\n')
            
        except Exception as e:
            return HttpResponse('<h1>Sorry, an error occured during form handling! <br /> Please check your form and try again. </h1>')
    return render(request, 'apply.html')
    

def kimAdmin(request):
    data = Apply.objects.filter()
    return render(request, 'admin.html', {'data': data})