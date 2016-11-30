#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from focus.models import *
from focus.forms import CommentForm


# Create your views here.

def global_setting(request):
	return {"SITE_NAME": settings.SITE_NAME,
			 "SITE_DESC": settings.SITE_DESC}


def index(request):
	#logger.info("hahaha zhe shi ge ceshi !")
	column_list = Column.objects.all()
	article_list = Article.objects.all()[0:1]
	return render(request,"index.html",locals())

def services(request):
	column_list = Column.objects.all()
	article = Article.objects.all()[1:0]
	return render(request,"services.html",locals())

def clients(request):
	return render(request,"clients.html",locals())

def add_user(request):
	if request.method == "POST":
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment_form.save()
			return HttpResponse("添加评论成功")

	else:
		user_form = CommentForm()
		return render(request,"nouser.html",locals())