from django.http import HttpResponse


def index(request):
    return HttpResponse("Ibira manda um quack para Kleyton!")