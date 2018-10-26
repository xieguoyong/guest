"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sign import views  # 导入sign应用views文件

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),  # 添加index/路径配置
    url(r'^login_action/$', views.login_action),     # 添加login_action/路径配置
    url(r'^event_manage/$', views.event_manage),  # 添加login_action/路径配置

    # 访问http://127.0.0.1:8000/  http://127.0.0.1:8000/event_manage/时均跳转登录页
    url(r'^$', views.index),
    url(r'^accounts/login/$', views.index),
]

