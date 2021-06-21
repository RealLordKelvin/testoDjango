from django.contrib import admin
from .models import FlowFile

# Register your models here.
#admin.site.register(FlowFile)
@admin.register(FlowFile)
class FlowFileAdmin(admin.ModelAdmin):
    search_fields = ['mpan','meter_id','reading_date_time','meter_registration_id']
    pass