#coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import login,logout,authenticate
from django.conf import settings
from focus.models import *
from focus.forms import *
from django.contrib.auth.hashers import make_password ###密码加密的处理方法
#from django.contrib.auth.decorators import login_required
import pdb


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
		comment_list = Comment.objects.order_by("-pub_date")[:3]
	except Exception as e:
		print e
	return render(request,"services.html",locals())


def do_reg(request):
	try:
		if request.method == "POST":
			reg_form = RegForm(request.POST)
			if reg_form.is_valid():
				"""注册"""
				user = NewUser.objects.create(username=reg_form.cleaned_data["username"],
				                           email = reg_form.cleaned_data["email"],
				                           #profile = reg_form.cleaned_data["profile"],
				                           password =make_password(reg_form.cleaned_data["password"]),)
				user.save()

				#登录
				user.backend="django.contrib.auth.backends.ModelBackend"###指定默认的登录验证方式
				login(request,user)
				print request.user
				return HttpResponseRedirect(request.POST.get("source_url"))  # 登录成功后重定向到之前的页面
			else:
				return render(request,"failure.html",{"reason":reg_form.errors})
		else:
			#request.session['reg_from'] = request.META.get('HTTP_REFERER', '/')
			reg_form = RegForm()
	except Exception as e:
		print e
	return  render(request,"reg.html",{"reg_form":reg_form})

def add_user(request):
	if request.method == "POST":
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment_form.save()
			return HttpResponseRedirect(request.POST.get("source_url"))

	else:
		user_form = CommentForm()
		return render(request,"nouser.html",locals())

def do_login(request):
	try:
		if request.method == "POST":
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				username = login_form.cleaned_data["username"]
				password = login_form.cleaned_data["password"]
				user = authenticate(username=username,password=password)###django提供的验证方法
				if user is not None and user.is_active:
					#user.backend = "django.contrib.auth.backend.ModelBackend"
					login(request,user)

					print bool(request.user.is_authenticated)
				else:
					return render(request, 'login.html', {"login_form":login_form, 'error': "password or username is not ture!"})
				return redirect(request.session['login_from'])  # 登录成功后重定向到之前的页面
			else:
				return render(request,"failure.html",{"reason":login_form.errors})
		else:
			request.session['login_from'] = request.META.get('HTTP_REFERER', '/')#记住get方法获得的页面，待会儿回到这个页面，没有就设置为主页
			login_form = LoginForm()
	except Exception as e:
		print e
	return render(request,"login.html",{"login_form":login_form})

#注销
def do_logout(request):
	try:
		logout(request)
	except Exception as e:
		print e
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))