from django.shortcuts import render, redirect
from .models import Contact_Us_Form
from django.contrib import messages
# Create your views here.
from .models import Contact_Us_Form, Cover_Photo, About, Skills, Resume, Services, Portfolio, Testimonials



def index(request):
    last_Cover_Photo = None
    last_About = None
    last_Resume = None


    last_Cover_Photo_query = Cover_Photo.objects.all()
    for j in last_Cover_Photo_query:
        last_Cover_Photo = j

    last_About_query = About.objects.all()
    for j in last_About_query:
        last_About = j


    last_Skills_query = Skills.objects.all()


    last_Resume_query = Resume.objects.all()
    for j in last_Resume_query:
        last_Resume = j

    last_Services_query = Services.objects.all()

    last_Portfolio_query = Portfolio.objects.all()

    last_Testimonials_query = Testimonials.objects.all()
    print(last_Testimonials_query)


    context = {'last_Cover_Photo':last_Cover_Photo, 'last_About':last_About, 'last_Skills_query':last_Skills_query, 'last_Resume':last_Resume, 'last_Services_query':last_Services_query, 'last_Testimonials_query':last_Testimonials_query, 'last_Portfolio_query':last_Portfolio_query}
    return render(request, 'index.html', context)



def submit_contact_us_form(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    var_Contact_Us = Contact_Us_Form(Name=name, Email=email, Subject=subject, Message=message)
    var_Contact_Us.save()
    messages.success(request, 'Message Has Sent Successfully !!')
    return redirect('/')