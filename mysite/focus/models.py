#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

###从django内置的一个user类继承
@python_2_unicode_compatible
class NewUser(AbstractUser):
	###username = models.CharField("username",max_length = 100)
	###email = models.EmailField()
	###password = models.CharField("password",max_length=16)
	###userinfo = models.OneToOneField(User)
	#join_time = models.DateTimeField()
	profile = models.CharField("profile",default = "",max_length = 256)

	def __str__(self):
		return self.username


###文章所属的分栏类
class Column(models.Model):
	name = models.CharField("column_name",max_length=256)
	intro = models.TextField("introductions",default = "")
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name = "分栏"
		verbose_name_plural = verbose_name
		ordering = ['name']

###文章类
class Article(models.Model):
	column = models.ForeignKey(Column,blank=True,null=True,verbose_name="belong to")
	title = models.CharField("title",max_length=256)
	author = models.ForeignKey("Author")
	content = models.TextField("content")
	user = models.ManyToManyField("NewUser",blank=True)
	pub_date = models.DateTimeField(auto_now_add=True,editable=True)
	update_time = models.DateTimeField(auto_now=True,null=True)
	published = models.BooleanField("notDraft",default=True)
	comment_num = models.IntegerField(default=0)
	keep_num = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title
	
	class Meta:
		verbose_name = "文章"
		verbose_name_plural = verbose_name

###文章需要的评论
class Comment(models.Model):
	user = models.ForeignKey("NewUser",null=True)
	article = models.ForeignKey(Article,null=True)
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True,editable=True)
	
	def __unicode__(self):
		return self.content
	class Meta:
		verbose_name = "评论"
		verbose_name_plural = verbose_name

###作者类
class Author(models.Model):
	name = models.CharField(max_length=256)
	profile = models.CharField("profile",default="",max_length=256)
	password = models.CharField("password",max_length=256)
	register_date = models.DateTimeField(auto_now_add=True,editable=True)

	
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name = "作者"
		verbose_name_plural = verbose_name