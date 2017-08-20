from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

'''
# Create your views here.
def index(request):
	return HttpResponse("Hello, world. This is my first App.")
'''

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)