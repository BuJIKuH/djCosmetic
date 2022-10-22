from django.contrib import admin

from .models import ProceduresModels, ProblemsModel, PartOfBodyModel, MastersModel

admin.site.register(ProceduresModels)
admin.site.register(ProblemsModel)
admin.site.register(PartOfBodyModel)
admin.site.register(MastersModel)
