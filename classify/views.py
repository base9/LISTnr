from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    message = request.GET.get('message', '')

    freq = {}
    nWords = 0
    for word in message.split():
      nWords += 1
      if word in freq:
        freq[word] += 1
      else:
        freq[word] = 1
         
    eventwords = 'event rsvp public pm am p.m. a.m. gather meet \
      party picnic rally parade barbecue festival happening get-together luncheon'

    probability = 0

    for word in eventwords.split():
      if word in freq:
        probability += 20*freq[word]


    print "I am {0} percent certain that this text describes an event.".format(probability)


    return HttpResponse(probability)

