from django.contrib import admin
from .models import TestModel
from time import sleep

# Register your models here.
@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'status')
    fields = ['name']
    actions = ['start', 'stop', 'clear']

    def start(self, request, queryset):
        for obj in queryset:
            result = obj.start()
            if result:
                self.message_user(request, result)
            sleep(0.1)

    def stop(self, request, queryset):
        for obj in queryset:
            result = obj.stop()
            if result:
                self.message_user(request, result)
            sleep(0.1)

    def clear(self, request, queryset):
        for obj in queryset:
            result = obj.clear()
            if result:
                self.message_user(request, result)
