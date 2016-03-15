#!/usr/bin/python
#-*-coding:utf-8-*-

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from website.models import McUsers
from website.forms.accountform import LoginForm,ChangePasswordForm
from django.views.decorators.csrf import csrf_protect
import logging

#Get an instance of a logger
#logger = logging.getLogger("website")

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('homepage'))
	state=None
	if request.method=="POST":
		account=request.POST.get("account")
		password=request.POST.get("password")
		user=auth.authenticate(username=account,password=password)
		if user is not None:
			auth.login(request,user)
			#logger.info(account+"已登录，登录时间:"+str(time.time()))
			return HttpResponseRedirect(reverse('homepage'))
		else:
			state="not_exist_or_password_error"
	content={
		"active_menu":"homepage",
		"state":state,
		"user":None
	}
	return render(request,"accounts/login.html",content)

def logout(request):
	#logger.info("注销！！！！")
	auth.logout(request)
	return HttpResponseRedirect(reverse("homepage"))

@login_required
def set_password(request):
	user=request.user
	state=None
	if request.method=="POST":
		old_password=request.POST.get("old_password","")
		new_password=request.POST.get("new_password","")
		repeat_password=request.POST.get("repeat_password","")
		if user.check_password(old_password):
			if not new_password:
				state="empty"
			elif new_password!=repeat_password:
				state="repeat_error"
			else:
				user.set_password(new_password)
				user.save()
				state="success"
		else:
			state="password_error"
	content={
		"user":user,
		"active_menu":"homepage",
		"state":state
	}
	return render(request,"accounts/set_password.html",content)



