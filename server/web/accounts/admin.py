from django.contrib import admin

from .models import ApiKey, Score

admin.site.register(ApiKey)
admin.site.register(Score)