from django.conf.urls import patterns, url,include
from django.contrib import admin
from website import views as website_views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^account/login/$', 'businesslogic.account.login',name="login"),
	url(r'^account/logout/$','businesslogic.account.logout',name="logout"),
	url(r'^account/set_password/$','businesslogic.account.set_password',name="set_password"),
]

