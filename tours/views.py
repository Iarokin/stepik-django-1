from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from tours import data, services


def main_view(request):
    info = services.random_cards(data.tours)
    return render(request, 'index.html', context={
        "tours": info,
        "title": data.title,
        "description": data.description,
        "subtitle": data.subtitle,
        "departures": data.departures})


def departure_view(request, departure):
    city = data.departures.get(departure)
    if city is None:
        raise Http404
    found = services.counter_tours(data.tours, departure)
    return render(request, 'departure.html', context={
        "infos": data.tours,
        "found": found,
        "title": data.title,
        "subtitle": data.subtitle,
        "departures": data.departures}
    )


def tour_view(request, id):
    if id is None or id < 1 or id > 16:
        raise Http404
    info = data.tours[id]
    return render(request, 'tour.html', context={
        "info": info,
        "title": data.title,
        "subtitle": data.subtitle,
        "departures": data.departures}
    )


def custom_handler404(request, exception):
    return HttpResponseNotFound('Данной страницы не существует. Попробуйте перейти к другой :).')


def custom_handler500(request, *args, **argv):
    return HttpResponse('Ошибка на стороне сервера')
