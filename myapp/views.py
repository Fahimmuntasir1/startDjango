from django.http import HttpResponse


def aboutUs(request):
    return HttpResponse("Wellcome to About page")


def courses(request):
    return HttpResponse("Wellcome to Courses page")
