from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

# To overide the order of fields


class TutorialAdmin(admin.ModelAdmin):
    # fields = ["tutorial_title",
    #           "tutorial_published",
    #           "tutorial_content"]

    # Use fieldsets if you would like organise headers
    fieldsets = [
        # Tuple of (Name of header, K,V of fields for list of fields)
        ("Title and date", {"fields": [
         "tutorial_title", "tutorial_published"]}),
        ("URL", {"fields": ["tutorial_slug"]}),
        ("Content", {"fields": ["tutorial_content"]}),
        ("Series", {"fields": ["tutorial_series"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)

admin.site.register(Tutorial, TutorialAdmin)
