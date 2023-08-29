from django.http import HttpResponse;
def homepage(request):
    print("home page")
    return HttpResponse("this is home page")
