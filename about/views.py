from django.shortcuts import render, HttpResponse
from .models import Apply

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
            return HttpResponse('<h1>Submitted successfully! We gonna contact you very soon and discuss the rest. Thank you <br/> <a href="/"> Click here to go back</a>')
        except Exception as e:
            return HttpResponse('<h1>Sorry, an error occured during form handling! <br /> Please check your form and try again. </h1>')
    return render(request, 'apply.html')
    

def kimAdmin(request):
    data = Apply.objects.filter()
    return render(request, 'admin.html', {'data': data})