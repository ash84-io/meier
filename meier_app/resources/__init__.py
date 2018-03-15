# -*- coding:utf-8 -*-
from .blog.post_detail_view import post_detail_view
from .blog.post_list_view import post_list_view
from .admin import admin_dashboard_view, admin_settings_view, admin_writer_view, admin_account_view

resource_blueprints = [
    post_list_view,
    post_detail_view,
    admin_dashboard_view,
    admin_settings_view,
    admin_writer_view,
    admin_account_view
]