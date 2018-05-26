from django.shortcuts import render
from .models import Feature, FeatureComment

# Create your views here.
def all_features(request):
    features = Feature.objects.all()
    return render(request, "features.html", {'features':features} )