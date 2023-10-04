from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Data
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Data
    template_name = 'search_results.html'

def index(request):
    return render(request, 'index.html')

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Data
    template_name = 'search_results.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Data.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(age__icontains=query)
        )
        return object_list