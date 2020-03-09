from django.urls import reverse_lazy
from django.views.generic import (ListView, TemplateView, CreateView, UpdateView, DeleteView, )
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import AuthUserForm, URLAddForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import URL


class AboutView(TemplateView):
    template_name = 'urlcheck/about.html'


class URLListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = URL
    template_name = 'urlcheck/url_list.html'
    context_object_name = 'url_list'
    queryset = URL.objects.all()


class UsiteLoginView(LoginView):
    model = User
    template_name = 'urlcheck/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('url_list')


class UsiteLogoutView(LogoutView):
    success_url = reverse_lazy('about')


class URLCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = URL
    form_class = URLAddForm
    template_name = 'urlcheck/url_form.html'
    success_url = reverse_lazy('url_list')


class URLDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = URL
    success_url = reverse_lazy('url_list')


class URLUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    template_name = 'urlcheck/url_form.html'
    form_class = URLAddForm
    model = URL
    success_url = reverse_lazy('url_list')
