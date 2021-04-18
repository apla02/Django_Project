from django.contrib import admin

from .models import Question, Choice
"""
option 1
admin.site.register(Question)
admin.site.register(Choice)
"""
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['published_date'],'classes':['collapse'] }),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
