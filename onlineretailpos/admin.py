from django.contrib import admin
from django.contrib.admin.apps import AdminConfig
from django.conf import settings



class MyAdminSite(admin.AdminSite):
    site_header = f"{settings.STORE_NAME} - Data Portal"
    site_title = "Online Retail POS"
    index_title = "Data Administration"


class MyAdminConfig(AdminConfig):
    default_site = 'onlineretailpos.admin.MyAdminSite'

