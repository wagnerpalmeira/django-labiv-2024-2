from django.contrib import admin
from .models.promotion import Promotion
from .models.comment import Comment

admin.site.register(Promotion)
admin.site.register(Comment)
