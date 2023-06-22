from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'sravani','age':21}
    return render(request,'jinja.html',context=d)