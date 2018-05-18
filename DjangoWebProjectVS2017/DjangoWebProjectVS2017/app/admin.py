
from django.contrib import admin
from app.models import Choice, Question, Topic

class TopicAdmin(admin.ModelAdmin):
    """Definition of the Topic editor."""
    fieldsets = [
        (None, {'fields': ['text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['text']
    date_hierarchy = 'pub_date'

admin.site.register(Topic, TopicAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    max = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Topic', {'fields': ['topic']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date')
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)