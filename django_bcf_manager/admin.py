from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(BcfFile)
admin.site.register(Project)
admin.site.register(Topic)
admin.register(TopicLabel)


