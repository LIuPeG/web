from django.contrib import admin
from django.db import models
from django import forms
from .models import Comment,Article,Column,Author,NewUser
# Register your models here.

class NewUserAdmin(admin.ModelAdmin):
	list_display = ('username',  'profile',)

class AuthorAdmin(admin.ModelAdmin):
	fields = ("name","profile",)

class CommentAdmin(admin.ModelAdmin):
	fields = ('pub_date', 'content')

class ColumnAdmin(admin.ModelAdmin):
	fields = ('name', 'intro')

	class Media:
		js = (
			"/static/js/kindeditor-4.1.7/kindeditor-min.js",
			"/static/js/kindeditor-4.1.7/lang/zh_CN.js",
			"/static/js/kindeditor-4.1.7/config.js",
		)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

    class Media:
	    js = (
		    "/static/js/kindeditor-4.1.7/kindeditor-min.js",
		    "/static/js/kindeditor-4.1.7/lang/zh_CN.js",
		    "/static/js/kindeditor-4.1.7/config.js",

	    )

admin.site.register(NewUser,NewUserAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Column,ColumnAdmin)
admin.site.register(Author,AuthorAdmin)