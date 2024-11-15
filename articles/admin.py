from django.contrib import admin
from .models import Article
# Register your models here.


class Admin_Settings(admin.ModelAdmin):
      list_display = ["title", "author", "add_date", "content", "upp_date"]
      list_filter = ["add_date", "author", "title"]
      search_fields = ["title", "author", "depart"]
      list_editable = ["content", "author"]


admin.site.register(Article, Admin_Settings)


