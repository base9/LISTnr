from django.shortcuts import render

from django.http import HttpResponse

import math

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
         
    eventWords = 'event rsvp public pm am p.m. a.m. gather meet \
      party picnic rally parade barbecue festival happening get-together luncheon'
    
    # in english: probability that this is an event email is determined by the number of 
    # words in the email that match one of the above eventWords.  Matches * (20 / math.ceil(nWords/100) )


    probability = 0

    for word in eventWords.split():
      if word in freq:
        probability += 20*freq[word]

    probability = probability / math.ceil(nWords/100)

    print "I am {0} percent certain that this text describes an event.".format(probability)


    return HttpResponse(probability)

