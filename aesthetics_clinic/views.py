from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProceduresModels, ProblemsModel, PartOfBodyModel, MastersModel


class PartOfBodyView(ListView):
    """Вывод частей тела"""
    model = PartOfBodyModel
    context_object_name = 'part_of_body'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PartOfBodyView, self).get_context_data(**kwargs)
        context['name'] = 'Части тела'
        return context

    def get_queryset(self):
        return PartOfBodyModel.objects.all()


class ProblemsView(ListView):
    """Вывод проблем с кожей"""
    model = ProblemsModel
    context_object_name = 'problems'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProblemsView, self).get_context_data(**kwargs)
        context['name'] = 'Проблемы'
        return context

    def get_queryset(self):
        return ProblemsModel.objects.all()


class MasterView(ListView):
    """Вывод мастеров"""
    model = MastersModel
    template_name = 'masters/masters.html'
    context_object_name = 'masters'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MasterView, self).get_context_data(**kwargs)
        context['second_name'] = 'Фамилия'
        return context

    def get_queryset(self):
        return MastersModel.objects.all()


class MasterViewDetail(DetailView):
    """Вывод мастера по slug"""
    model = MastersModel
    template_name = 'masters/master_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'item'


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
    context_object_name = 'item'
