#!/usr/bin/python
#-*-coding:utf-8-*-

from django import forms
#from captcha.fields import CaptchaField
from website.businesslogic.fields import AccountField,PasswordField,UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from website.models import McAction,McMediainfo,McRole,McRoleAction,McSpiderRule,McUserRole,\
	McUsers,STATUS_CHOICES,SEX_CHOICES,IS_ACTIVE_CHOICES
import traceback

class LoginForm(forms.Form):
	username=AccountField(required=True,max_length=12,min_length=6)
	password=PasswordField(required=True,max_length=12,min_length=6)

	def login(req):
		if req.method=="POST":
			uf=LoginForm(req.POST)
			if uf.is_valid():
				#获得表单数据
				username=uf.clean_data["username"]
				password=uf.clean_data["password"]
				#获取的表单数据与数据库进行比较
				user=McUsers.objects.filter(username_exact=username,password_exact=password)
				if user:
					#比较成功，跳转index
					response=HttpResponseRedirect("/index/")
					#将username写入cookie,失效时间为2小时
					response.set_cookie("username",username)
					return response
				else:
					#比较失败
					return HttpResponseRedirect('/login/')
		else:
			uf=LoginForm()
		return render_to_response("login.html",{"uf",uf},context_instance=RequestContext(req))

	def index(req):
		username=req.COOKIES.get("username","")
		return render_to_response("index.html",{"username",username})

	def logout(req):
		response=HttpResponse("logout!!")
		#清理cookie里保存username
		response.delete_cookie("username")
		return response


class ChangePasswordForm(forms.Form):
	newpassword=PasswordField(required=True,max_length=12,min_length=6)
	renewpassword=PasswordField(required=True,max_length=12,min_length=6)

	def __init__(self,user,*args,**kwargs):
		self.user=user
		super(ChangePasswordForm,self).__init__(*args,**kwargs)

	def clean_password2(self):
		newpassword=self.clean_data.get("newpassword")
		renewpassword=self.clean_data.get("renewpassword")
		if newpassword and renewpassword:
			if newpassword!=renewpassword:
				raise forms.ValidationError(u"俩次密码输入不一致,请重新输入!")
		raise forms.ValidationError(u"俩次密码输入不一致,请重新输入!")
		return renewpassword

	def save(self):
		self.user.set_password(self.clean_data["newpassword"])
		try:
			if commit:
				self.user.save()#提交修改至数据库
			return self.user
		except Exception, e:
			raise e
		
class UserForm(forms.Form):
	account=AccountField(required=True)
	password=PasswordField(required=True)
	username=UsernameField(required=True)
	email=forms.CharField(required=True)
	status=forms.ChoiceField(required=True,choices=STATUS_CHOICES,error_messages={'invalid':u'请正确选择下拉框'})
	isadmin=forms.ChoiceField(required=True,choices=STATUS_CHOICES,error_messages={'invalid':u'请正确选择下拉框'})

	def add(req):
		if req.method=="POST":
			uf=UserForm(req.POST)
			if uf.is_valid:
				#获取表单数据
				account=uf.clean_data["account"]
				password=uf.clean_data["password"]
				username=uf.clean_data["username"]
				email=uf.clean_data["email"]
				status=uf.clean_data["status"]
				isadmin=uf.clean_data["isadmin"]

				#添加到数据库
				McUsers.objects.create(account=account,username=username,password=password,email=email,status=status,isadmin=isadmin)
				return HttpResponse("add success!")
		else:
			uf=UserForm()
		return render_to_response("signup.html",{"uf",uf})