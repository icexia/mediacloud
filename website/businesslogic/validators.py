#!/usr/bin/python
#-*-coding:utf-8-*-

import re
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

account_re = re.compile(r'^([\w]{9}|[a-zA-Z]{1}[\w]+?)$')
account = RegexValidator(account_re,u'您的账号,由字母数字下划线组成,首字母为字母','invalid')

password_re = re.compile(r'^[\w]+?$')
password = RegexValidator(password_re,u'密码由字母数字下划线组成的字符串，最少为6位','invalid')

title_re=re.compile(r'[\w]')
title=RegexValidator(title_re,u'标题不能为空','invalid')

username_re = re.compile(r'^[\u4e00-\u9fa5]{2,6}$')
class UsernameValidator(object):
	message = u'姓名必须是2-6个汉字'
	code = 'invalid'

	def __init__(self, message=None, code=None):
		if message is not None:
			self.message = message
		if code is not None:
			self.code = code

	def __call__(self,value):
		if not all([True if i >= u'\u4e00' and i <= u'\u9fa5' else False for i in value]):
			raise ValidationError(self.message, code=self.code)
			
username=UsernameValidator()
		