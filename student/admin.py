# coding utf - 8
from django.contrib import admin
from student.models import *

# class StudAdmin(admin.ModelAdmin):
# 	# fields = ['Group','birth_date','name','surname','name2','ticket']
# 	fieldsets = {
# 		(None,{'fields':('Group')
# 			}),

# 		('Information',{
# 			'fields':('name','surname','name2','ticket')
# 			}),

# 		('Birth_Day',{
# 			'fields':'birth_date'
# 			}),

# 	}
# class StudAdmin(admin.ModelAdmin): 
#  	pass	
admin.site.register(Stud)
admin.site.register(Group)
