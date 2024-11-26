from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def reprocessing(request):
    return render(request, 'reprocessing.html')