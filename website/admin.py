from django.contrib import admin
from .models import Blink, Task, BlinkNotes

# Register your models here.
admin.site.register(Blink)
admin.site.register(BlinkNotes)
admin.site.register(Task)