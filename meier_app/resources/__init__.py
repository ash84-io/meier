# -*- coding:utf-8 -*-
from .admin import admin_contents_api
from .admin import (
    admin_dashboard_view,
    admin_settings_view,
    admin_writer_view,
    admin_user_view,
    admin_contents_view,
)
from .admin import admin_index_view
from .admin import admin_settings_api
from .admin import admin_user_api
from .admin import admin_writer_view, admin_writer_api
from .blog.post_detail_view import post_detail_view
from .blog.post_list_view import post_list_view
from .blog.tag_list_view import tag_list_view
from .blog.assets import assets
from .blog.rss import rss

resource_blueprints = [
    rss,
    assets,
    tag_list_view,
    post_list_view,
    post_detail_view,
    admin_index_view,
    admin_dashboard_view,
    admin_settings_api,
    admin_settings_view,
    admin_writer_api,
    admin_writer_view,
    admin_user_view,
    admin_user_api,
    admin_contents_api,
    admin_contents_view,
]
