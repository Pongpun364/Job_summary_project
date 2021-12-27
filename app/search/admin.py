from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

from .models import Job, TextTemplate

# Apply summernote to all TextField in model.
class TextTemplateAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('body',)


admin.site.register(TextTemplate, TextTemplateAdmin)
admin.site.register(Job)