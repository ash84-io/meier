# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from meier_app.models.user import User
from meier_app.models.settings import Settings

admin_settings_view = Blueprint('admin_settings_view', __name__, url_prefix='/admin/settings')


@admin_settings_view.route('/', methods=['GET'])
@jwt_required
def get_settings_view():
    settings = Settings.query.first()
    user = User.query.filter(User.email == get_jwt_identity()).scalar()
    return render_template("/admin/settings.j2",
                           title="Settings",
                           blog_title=settings.blog_title,
                           post_per_page=settings.post_per_page,
                           blog_desc=settings.blog_desc,
                           theme=settings.theme,
                           current_user=user)

