# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask_jwt_extended import jwt_required, get_jwt_identity

from meier_app.models.settings import Settings
from meier_app.models.user import User

admin_writer_view = Blueprint('admin_writer_view', __name__, url_prefix='/admin/writer')


@admin_writer_view.route('/', methods=['GET'])
@jwt_required
def get_new_writer_view():
    settings = Settings.query.first()
    user = User.query.filter(User.email == get_jwt_identity()).scalar()
    return render_template("/admin/writer.j2",
                           title="Writer",
                           blog_title=settings.blog_title,
                           current_user=user)

