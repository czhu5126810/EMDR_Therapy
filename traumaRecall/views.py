from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def traumaRecall(request):
    return render(request, 'traumaRecall.html')