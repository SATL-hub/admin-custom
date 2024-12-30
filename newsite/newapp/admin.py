from django.contrib import admin
from. models import *
from django.utils.html import format_html
from django.urls import path,reverse
from django.db.models import Avg
from django.shortcuts import render
import json
# Register your models here.
admin.site.site_title = "College site admin "
admin.site.site_header = "College administration"
admin.site.index_title = "Site administration"
   
class studentdetailsAdmin(admin.ModelAdmin):
    search_fields=('name','department__name')
    ordering = ('name',)
    list_display=('name','department','mark','age')
    
    def mark(self,obj):
        return self.style_mark(obj.marks)
    
    def style_mark(self,m):
        if m>=48:
            return format_html('<span style="color: green; font-weight: bold;">{}</span>', m)
        else:
            return format_html('<span style="color: red; font-weight:bold;">{}</span>',m)
    mark.admin_order_field = 'marks'
    #remove delete button
    def has_delete_permission(self, request, obj = None): 
        return False
    def has_add_permission(self,request,obj=None):
        return False
    def has_change_permission(self,request,obj=None):
        return False
    class MarkFilter(admin.SimpleListFilter):
        title = 'Marks'  # Display name for the filter in the admin
        parameter_name = 'marks'  # URL parameter for the filter

        def lookups(self, request, model_admin):
        
            return (
            ('passed', 'Passed'),
            ('failed', 'Failed'),
            )
        def queryset(self, request, queryset):
       
            if self.value() == 'passed':
                return queryset.filter(marks__gte=48)  # Marks greater than or equal to 48
            if self.value() == 'failed':
                return queryset.filter(marks__lt=48)  # Marks less than 48
            return queryset
    
    list_filter=('department',MarkFilter,)
   
    readonly_fields=('age',)

    #chart---------------------------------------------------------------------------------------------------------------------
   
    def changelist_view(self, request):
        # Fetch data for the chart
        data = (
            student_details.objects.values('department__name')
            .annotate(average_marks=Avg('marks'))
            .order_by('department__name')
        )
        departments = [item['department__name'] for item in data]
        marks = [round(item['average_marks']) for item in data]
        extra_context =  {}
        extra_context['departments'] = departments
        extra_context['marks'] = marks
        return super().changelist_view(request, extra_context=extra_context)

 
admin.site.register(departments)
admin.site.register(student_details,studentdetailsAdmin)