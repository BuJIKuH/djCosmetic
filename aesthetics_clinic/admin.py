from django.contrib import admin

from .models import ProceduresModels, ProblemsModel, PartOfBodyModel, MastersModel


class PartOfBodyAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProceduresAdmin(admin.ModelAdmin):
    list_filter = ('price',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProblemsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class MastersAdmin(admin.ModelAdmin):
    list_filter = ('first_name',)
    search_fields = ('second_name',)
    prepopulated_fields = {'slug': ('second_name',)}


admin.site.register(ProceduresModels, ProceduresAdmin)
admin.site.register(ProblemsModel, ProblemsAdmin)
admin.site.register(PartOfBodyModel, PartOfBodyAdmin)
admin.site.register(MastersModel, MastersAdmin)
