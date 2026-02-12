from django.shortcuts import render
from .models import File
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FileForm


class FileListView(ListView):
    model = File
    template_name = 'files.html'
    context_object_name = 'files'


class FileDetailView(DetailView):
    model = File
    template_name = 'file_detail.html'
    context_object_name = 'file'
    

class FileCreateView(LoginRequiredMixin, CreateView):
    model = File
    template_name = 'file_create.html'
    fields = ['name', 'main_content']
    login_url = 'login-page'
    success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
class FileUpdateView(LoginRequiredMixin, UpdateView):
    model = File
    template_name = 'update.html'
    fields = ['name', 'main_content']
    login_url = 'login-page'
    success_url = '/'

    def get_queryset(self):
        return File.objects.filter(created_by=self.request.user)
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return super().form_valid(form)

class FileDeleteView(LoginRequiredMixin, DeleteView):
    model = File
    template_name = 'delete.html'
    success_url = '/'
    login_url = 'login-page'