from django.contrib import admin
from .models import Template, Balaji_IdCard


class BalajiIdCardAdmin(admin.ModelAdmin):
    list_display = ('name','father_name','course','dob','image','pk')
admin.site.register(Balaji_IdCard, BalajiIdCardAdmin)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('template','pk')
admin.site.register(Template,TemplateAdmin)