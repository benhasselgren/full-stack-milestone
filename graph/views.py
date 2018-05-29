from django.contrib.auth import get_user_model
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Max

from bugs.models import Bug
from features.models import Feature

# Create your views here.
User = get_user_model()

def graph(request):
    return render(request, 'graphs.html')


def number_of_graph(request):
    user_count = User.objects.all().count()
    bug_count = Bug.objects.all().count()
    feature_count = Feature.objects.all().count()
    bug_max = Bug.objects.all().aggregate(Max('upvotes'))
    feature_max = Feature.objects.all().aggregate(Max('upvotes'))
    
     
    features_max_upvote = feature_max
    labels1 = ["Users", "Bugs", "Features"]
    labels2 = ["Bugs", "Features"]
    default = [user_count, bug_count, feature_count]
    max_values = [bug_max["upvotes__max"], feature_max["upvotes__max"]]
    
    data={
        "labels1": labels1,
        "labels2": labels2,
        "default": default,
        "max_values": max_values
    }
    return JsonResponse(data, safe=False)