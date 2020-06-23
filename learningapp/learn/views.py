from django.shortcuts import render
from .forms import TeachingContentForm
from .models import TeachingContent
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin




class IndexPageView(TemplateView):
    template_name = 'learn/index.html'


class ContentCreateView(CreateView):
    model = TeachingContent
    form_class = TeachingContentForm
    template_name = 'learn/content_form.html'


class ContentDetailView(DetailView):
    model = TeachingContent
    context_object_name = 'content'
    template_name = 'learn/content_detail.html'


class ContentUpdateView(UpdateView):
    model = TeachingContent
    form_class = TeachingContentForm
    template_name = 'learn/content_update.html'


class ContentListView(LoginRequiredMixin, ListView):
    model = TeachingContent
    template_name = 'learn/content_list.html'
    context_object_name = 'content'
    paginate_by = 5