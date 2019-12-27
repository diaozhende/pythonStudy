from django.contrib import admin
from book.models import BookModel,BookRole
# Register your models here.
admin.site.register(BookModel)
admin.site.register(BookRole)
