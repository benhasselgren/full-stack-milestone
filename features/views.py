from django.shortcuts import render, get_object_or_404
from .models import Feature, FeatureComment

# Create your views here.
def all_features(request):
    features = Feature.objects.all()
    return render(request, "features.html", {'features':features} )
    
def feature_detail(request, pk):
    """
    Create a view that returns a single
    bug object based on the bug ID (pk) and
    render it to the bug_detail.html template
    or return 404 error if object is not found
    """
    feature = get_object_or_404(Feature, pk=pk)
    comments = FeatureComment.objects.filter(feature__pk=feature.pk)
    comments_total = len(comments)
    feature.views += 1
    feature.save()
    return render(request, 'feature_detail.html', {'feature':feature, 'comments':comments, 'comments_total':comments_total})