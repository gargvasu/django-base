from django.conf.urls import url
from user import views

app_name = 'user'

urlpatterns=[
	url(r'^register/$',views.register,name='register'),
	url(r'^login/$',views.login,name='login'),
	url(r'^special/',views.special,name='special'),
	url(r'^logout/$', views.user_logout, name='logout'),
]