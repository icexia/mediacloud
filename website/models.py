#!/usr/bin/python
#-*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICES=(
	('0','无效'),
	('1','有效'),
	)

SEX_CHOICES = (
	('0','男'),
	('1','女'),
)

IS_ACTIVE_CHOICES=(
	('0','否'),
	('1','是'),
	)

class McAction(models.Model):
	action_id = models.AutoField(primary_key=True)
	action_name = models.CharField(max_length=40, blank=True, null=True)
	status = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'MC_Action'


class McMediainfo(models.Model):
	page_url = models.CharField(unique=True, max_length=80, blank=True, null=True)
	title = models.CharField(max_length=64, blank=True, null=True)
	ename = models.CharField(db_column='eName', max_length=64, blank=True, null=True)  # Field name made lowercase.
	othername = models.CharField(db_column='otherName', max_length=200, blank=True, null=True)  # Field name made lowercase.
	adaptor = models.CharField(max_length=200, blank=True, null=True)
	director = models.CharField(max_length=200, blank=True, null=True)
	leader = models.CharField(max_length=500, blank=True, null=True)
	kind = models.CharField(max_length=200, blank=True, null=True)
	language = models.CharField(max_length=40, blank=True, null=True)
	duration = models.CharField(max_length=10, blank=True, null=True)
	story = models.CharField(max_length=500, blank=True, null=True)
	keyword = models.CharField(db_column='keyWord', max_length=150, blank=True, null=True)  # Field name made lowercase.
	productperson = models.CharField(db_column='productPerson', max_length=200, blank=True, null=True)  # Field name made lowercase.
	dubbing = models.CharField(max_length=200, blank=True, null=True)
	executiver = models.CharField(max_length=200, blank=True, null=True)
	original = models.CharField(max_length=200, blank=True, null=True)
	productcoltd = models.CharField(db_column='productColtd', max_length=255, blank=True, null=True)  # Field name made lowercase.
	productiontime = models.CharField(db_column='productionTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
	licence = models.CharField(max_length=200, blank=True, null=True)
	registration = models.CharField(max_length=200, blank=True, null=True)
	distributcoltd = models.CharField(db_column='distributColtd', max_length=200, blank=True, null=True)  # Field name made lowercase.
	totalnumber = models.CharField(db_column='totalNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
	updateinfo = models.CharField(db_column='updateInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
	area = models.CharField(max_length=40, blank=True, null=True)
	source = models.CharField(max_length=20, blank=True, null=True)
	createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
	updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
	updator = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'MC_MediaInfo'


class McRole(models.Model):
	role_id = models.AutoField(primary_key=True)
	role_name = models.CharField(max_length=100, blank=True, null=True)
	role_desc = models.CharField(max_length=255, blank=True, null=True)
	status = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'MC_Role'


class McRoleAction(models.Model):
	role_id = models.IntegerField(blank=True, null=True)
	action_id = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'MC_Role_Action'


class McSpiderRule(models.Model):
	spider_name = models.CharField(max_length=40, blank=True, null=True)
	start_urls = models.CharField(max_length=400, blank=True, null=True)
	allowed_domains = models.CharField(max_length=400, blank=True, null=True)
	restrict_xpaths = models.CharField(max_length=400, blank=True, null=True)
	allow_url = models.CharField(max_length=400, blank=True, null=True)
	next_page_xpath = models.CharField(max_length=400, blank=True, null=True)
	title_xpath = models.CharField(max_length=400, blank=True, null=True)
	e_name_xpath = models.CharField(max_length=400, blank=True, null=True)
	other_name_xpath = models.CharField(max_length=400, blank=True, null=True)
	adaptor_xpath = models.CharField(max_length=400, blank=True, null=True)
	director_xpath = models.CharField(max_length=400, blank=True, null=True)
	leader_xpath = models.CharField(max_length=400, blank=True, null=True)
	kind_xpath = models.CharField(max_length=400, blank=True, null=True)
	language_xpath = models.CharField(max_length=400, blank=True, null=True)
	duration_xpath = models.CharField(max_length=400, blank=True, null=True)
	story_xpath = models.CharField(max_length=400, blank=True, null=True)
	keyword_xpath = models.CharField(db_column='keyWord_xpath', max_length=400, blank=True, null=True)  # Field name made lowercase.
	product_person_xpath = models.CharField(max_length=400, blank=True, null=True)
	dubbing_xpath = models.CharField(max_length=400, blank=True, null=True)
	executiver_xpath = models.CharField(max_length=400, blank=True, null=True)
	original_xpath = models.CharField(max_length=400, blank=True, null=True)
	productcoltd_xpath = models.CharField(db_column='productColtd_xpath', max_length=400, blank=True, null=True)  # Field name made lowercase.
	production_time_xpath = models.CharField(max_length=400, blank=True, null=True)
	licence_xpath = models.CharField(max_length=400, blank=True, null=True)
	registration_xpath = models.CharField(max_length=400, blank=True, null=True)
	distributcoltd_xpath = models.CharField(db_column='distributColtd_xpath', max_length=400, blank=True, null=True)  # Field name made lowercase.
	totalnumber_xpath = models.CharField(db_column='totalNumber_xpath', max_length=400, blank=True, null=True)  # Field name made lowercase.
	updateinfo_xpath = models.CharField(db_column='updateInfo_xpath', max_length=400, blank=True, null=True)  # Field name made lowercase.
	area_xpath = models.CharField(max_length=400, blank=True, null=True)
	status = models.IntegerField(blank=True, null=True)
	spider_desc = models.CharField(max_length=20, blank=True, null=True)
	create_time = models.DateTimeField(blank=True, null=True)
	updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
	creator = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'MC_Spider_Rule'


class McUserRole(models.Model):
	role_id = models.IntegerField(blank=True, null=True)
	uid = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'MC_User_Role'


class McUsers(models.Model):
	uid = models.AutoField(primary_key=True)
	account = models.CharField(max_length=20, blank=True, null=True)
	password = models.CharField(max_length=64, blank=True, null=True)
	status = models.IntegerField(blank=True, null=True)
	username = models.CharField(db_column='userName', max_length=20, blank=True, null=True)  # Field name made lowercase.
	email = models.CharField(max_length=32, blank=True, null=True)
	isadmin = models.IntegerField(db_column='isAdmin', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'MC_Users'

	def __unicode__(self):
		return self.username
