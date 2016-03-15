#!/usr/bin/python
#-*-coding:utf-8-*-

from django.forms.fields import Field,CharField
from validators import account,username,password,title

class AccountField(CharField):
	default_error_messages = {
		'invalid':u'您的账号号,管理员:6-12位,由字母数字下划线组成,首字母为字母',
		'required':u'账号必填(由字母数字下划线组成)',
		'max_length':u'管理员用户名至多为12位'
	}
	default_validators = [account]

	def clean(self,value):
		value = self.to_python(value).strip()
		return super(AccountField, self).clean(value)

class PasswordField(CharField):
	default_error_messages = {
		'invalid':u'密码由字母数字下划线组成的字符串，最少为8位',
		'required':u'密码必须要填(由字母数字下划线组成的字符串，最少为6位)',
		'max_length':u'密码至多为16位',
		'min_length':u'密码至少为8位'
	}
	default_validators = [password]

class TitleField(CharField):
	default_error_messages={
		'invalid':u'标题不能为空！',
		'required':u'标题必填',
		'max_length':u'标题至少1位'
	}
	default_validators = [title]

class UsernameField(CharField):
	default_error_messages = {
		'invalid':u'同学姓名必须是2-4个汉字',
		'required':u'同学姓名必须要填（2-4个汉字）',
	}
	default_validators = [username]

	def clean(self,value):
		value = self.to_python(value).strip()
		return super(UsernameField, self).clean(value)
		