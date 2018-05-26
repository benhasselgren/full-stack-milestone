from django.shortcuts import render, get_object_or_404
from .models import Bug, BugComment

# Create your views here.
def all_bugs(request):
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {'bugs':bugs} )
    
def bug_detail(request, pk):
    """
    Create a view that returns a single
    bug object based on the bug ID (pk) and
    render it to the bug_detail.html template
    or return 404 error if object is not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    comments = BugComment.objects.filter(bug__pk=bug.pk)
    comments_total = len(comments)
    bug.views += 1
    bug.save()
    return render(request, 'bug_detail.html', {'bug':bug, 'comments':comments, 'comments_total':comments_total})