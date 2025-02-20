from django.contrib import admin

from agency.models import Newspaper, Topic, Redactor


class AdminRedactor(admin.ModelAdmin):
    list_display = ["username"]


admin.site.register(Newspaper)
admin.site.register(Topic)
admin.site.register(Redactor, AdminRedactor)
