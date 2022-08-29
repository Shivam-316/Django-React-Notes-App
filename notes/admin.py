from django.contrib import admin
from .models import Note
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on',)

admin.site.register(Note, NoteAdmin)