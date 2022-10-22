from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProceduresModels, ProblemsModel, PartOfBodyModel, MastersModel


class ProceduresView(ListView):
    """Вывод всех процедур"""
    model = ProceduresModels
    template_name = 'procedures/procedures.html'
    context_object_name = 'procedure'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProceduresView, self).get_context_data(**kwargs)
        context['title'] = 'Процедуры'
        return context

    def get_queryset(self):
        return ProceduresModels.objects.all()


class ProceduresViewDetail(DetailView):
    """Вывод процедуры по slug"""
    model = ProceduresModels
    template_name = 'procedures/procedures_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'procedure'