from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict={"insert_me":"i am from HTML"}
    return render (request, "fst_project/index.html", context= my_dict)
