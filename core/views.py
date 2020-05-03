from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class CityDetailView(DetailView):
    queryset = models.City.objects.all()
    context_object_name = 'obejct'
    template_name = 'core/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = models.City
    form_class = forms.CityForm
    template_name = 'core/add.html'
    success_url = reverse_lazy('core:home_page')
    success_message = "Город успешно создан"


class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = models.City
    form_class = forms.CityForm
    template_name = 'core/update.html'
    success_url = reverse_lazy('core:home_page')
    success_message = "Город успешно отредактирован"


class CityDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = models.City
    #template_name = 'core/delete.html'
    success_url = reverse_lazy('core:home_page')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Город успешно удален")
        return self.post(request, *args, **kwargs)


def home_page(request):
    cities = models.City.objects.all()
    paginator = Paginator(cities, 5)
    page_number = request.GET.get('page')
    cities = paginator.get_page(page_number)
    num_pages = paginator.page_range

    return render(request, 'core/home_page.html', {'cities': cities,
                                                    'num_pages': num_pages,
                                                    'paginator': paginator})
