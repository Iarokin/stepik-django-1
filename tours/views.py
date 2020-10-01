from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

departures = {"msk": "Москвы",
              "spb": "Петербурга",
              "nsk": "Новосибирска",
              "ekb": "Екатеринбурга",
              "kazan": "Казани"}


# Create your views here.
def MainView(request):
    return render(request, 'index.html')


def DepartureView(request, departure):
    city = departures.get(departure)
    if city is None:
        raise Http404
    return render(request, 'departure.html', context={
        'name': city
    })


def TourView(request, id):
    tour = id
    return render(request, 'tour.html', context={'tour': tour})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Данной страницы не существует. Попробуйте перейти к другой :).')


def custom_handler500(request, *args, **argv):
    return HttpResponse('Ошибка на стороне сервера')
