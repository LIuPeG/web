#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.conf import settings
from focus.models import *
from focus.forms import *
from django.contrib.auth.hashers import make_password ###密码加密的处理方法


# Create your views here.

def global_setting(request):
	return {"SITE_NAME": settings.SITE_NAME,
			 "SITE_DESC": settings.SITE_DESC}


def index(request):
	#logger.info("hahaha zhe shi ge ceshi !")
	try:
		column_list = Column.objects.all()
		article_list = Article.objects.all()[0:1]
		comment_list = Comment.objects.order_by("-pub_date")[:3]
	except Exception as e:
		return render(request,"404.html")
	return render(request,"index.html",locals())

def services(request):
	try:
		column_list = Column.objects.all()
		article = Article.objects.all()[1:0]
	except Exception as e:
		print e
	return render(request,"services.html",locals())

def do_reg(request):
	try:
		if request.method == "POST":
			reg_form = RegForm(request.POST)
			if reg_form.is_valid():
				"""注册"""
				user = User.objects.create(username=reg_form.cleaned_data["username"],
				                           email = reg_form.cleaned_data["email"],
				                           url = reg_form.cleaned_data["url"],
				                           password =make_password(reg_form.cleaned_data["password"]),)
				user.save()

				#登录
				user.backend="django.contrib.auth.backends.ModelBackend"###指定默认的登录验证方式
				login(request,user)
				return redirect(request.POST.get("source_url"))
			else:
				return render(request,"failure.html",{"reason":reg_form.errors})
		else:
			reg_form = RegForm()
	except Exception as e:
		print e
	return  render(request,"reg.html",locals())

def add_user(request):
	if request.method == "POST":
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment_form.save()
			return HttpResponse("添加评论成功")

	else:
		user_form = CommentForm()
		return render(request,"nouser.html",locals())

def do_login(request):
	try:
		if request.method == "POST":
			login_form = LoginForm()
			if login_form.is_valid():
				username = login_form.cleaned_data["username"]
				password = login_form.cleaner_data["password"]
				user = authenticate(username = username,password = password)###django提供的验证方法
				if user is None:
					user.backend = "django.contrib.auth.backendd.ModelBackend"
					login(request,user)
				else:
					return render(request,"failure.html",{"reason":"登录验证失败"})
				return redirect(request.POST.get("index"))
			else:
				return render(request,"failure.html",{"reason":login_form.errors})
		else:
			login_form = LoginForm()
	except Exception as e:
		print e
	return render(request,"login.html",locals())

#注销
def do_logout(request):
	try:
		logout(request)
	except Exception as e:
		print e
	return render(request.META["HTTP_REFERER"])