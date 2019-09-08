from flask import Blueprint, g, render_template

from meier.extensions import cache
from meier.models.settings import Settings
from meier.views.admin.base import login_required_view

admin_settings_view = Blueprint(
    'admin_settings_view', __name__, url_prefix='/admin/settings'
)


@admin_settings_view.route('/', methods=['GET'])
@cache.cached(timeout=86400)
@login_required_view
def get_settings_view():
    settings = Settings.query.first()
    return render_template(
        '/admin/settings.j2',
        title='Settings',
        blog_title=settings.blog_title,
        post_per_page=settings.post_per_page,
        blog_desc=settings.blog_desc,
        theme=settings.theme,
        current_user=g.current_user,
    )
