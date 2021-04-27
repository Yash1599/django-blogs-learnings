from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request ,*args , **kwargs):
    # return HttpResponse("<h1>Hello</h1>")
    return render(request , "home.html" , {})



def contact_view(request , *args , **kwargs):
    # my_title={
    #     "title_my" : "HI, Coders",
    #     "no_my" : 1599,
    # }
    return render(request , "about.html" , {})


def about_view(request , *args , **kwargs):
    my_title={
        "title_my" : "HI, Coders",
        "no_my" : 1599,
        "my_list" : [100,300,700]
    }
    return render(request , "about.html" , my_title)

