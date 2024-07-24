from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    return render(request=request, template_name="home.html", context={})

def contact_view(request, *args, **kwargs):
    return render(request=request, template_name="contact.html", context={})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 456, 789],
    }

    return render(request=request, template_name="about.html", context=my_context)

def social_view(request, *args, **kwargs):
    return render(request=request, template_name="social.html", context={})