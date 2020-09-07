import json
from django.shortcuts import HttpResponse
from .models import Review

def upvote(request):
    Review.num_vote_up += 1
    # Do your upvote here
    # Optionally return a message with new count of votes
    result = {
        'votes': 32,
        'success': True
    }
    return HttpResponse(json.dumps(result), content_type="application/json")
