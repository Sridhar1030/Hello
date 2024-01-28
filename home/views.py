from django.shortcuts import render , HttpResponse



def index(request):
    context = {
        'variables':"World",
        'var':"hello"
    }
    return render(request, 'index.html', context)

    # return HttpResponse("this is home page")
def about(request):
    return HttpResponse("Hello World")