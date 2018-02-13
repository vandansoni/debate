from django.contrib import admin
from Discussion.models import *

# Register your models here.


class DiscussionAdmin(admin.ModelAdmin):

	fieldsets = (
	    ('Discussion data', {'fields': ('title', 'text', 'discussion_type', 'image')}),
	    ('Date', {'fields': ('created_date',)}),
	)

	exclude = ('modified_date',)

	search_fields = ('title',)
	ordering = ('-created_date',)
	list_display = ('title', 'discussion_type','added_by')
	list_display_links = ('title', 'discussion_type')
	list_filter = ('discussion_type', )


class CommentAdmin(admin.ModelAdmin):


	exclude = ('modified_date',)


	list_display = ('text', 'discussion','added_by')
	
admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Comment,CommentAdmin)
