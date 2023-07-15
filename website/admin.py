from django.contrib import admin
from website.models import Lead
# Register your models here.
    
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['lead_name', 'lead_phone', 'membership', 'comment']



