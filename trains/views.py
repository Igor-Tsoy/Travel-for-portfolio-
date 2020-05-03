from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Train
from .forms import TrainForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


def home_page(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 5)
    page_number = request.GET.get('page')
    trains = paginator.get_page(page_number)
    num_pages = paginator.page_range

    return render(request, 'train/home_page.html', { 'trains': trains,
                                                      'num_pages': num_pages,
                                                      'paginator': paginator
                                                      })


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'train/add.html'
    success_url = reverse_lazy('train:home')
    success_message = "Поезд успешно создан"


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name = 'obejct'
    template_name = 'train/detail.html'


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Train
    form_class = TrainForm
    template_name = 'train/update.html'
    success_url = reverse_lazy('train:home')
    success_message = "Город успешно отредактирован"


class TrainDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Train
    #template_name = 'core/delete.html'
    success_url = reverse_lazy('train:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Город успешно удален")
        return self.post(request, *args, **kwargs)