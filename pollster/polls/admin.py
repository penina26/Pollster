from django.contrib import admin
from django.contrib.admin.helpers import Fieldset

from .models import Question, Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster admin Area"
admin.site.index_title = "Welcome to Pollster admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    Fieldsets =[(None, {'fields':['question_text']}),
    ('date Information',{'fields':['pub_date'], 
    'classes':['collapse']}),]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)