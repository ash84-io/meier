from flask import render_template
from os.path import join as path_join
base_helper_path = '/blog/helper'
from meier_app.commons.logger import logger

def blog_title_helper(blog_title):
    return render_template(path_join(base_helper_path, 'header/blog_title.j2'), blog_title=blog_title)

def blog_desc_helper(blog_desc):
    return render_template(path_join(base_helper_path, 'header/blog_desc.j2'), blog_desc=blog_desc)

def blog_link_helper(blog_link):
    return render_template(path_join(base_helper_path, 'header/blog_link.j2'), blog_link=blog_link)

def post_content_helper(post):
    global base_helper_path
    return render_template(path_join(base_helper_path, 'body/post/post_detail/post_content.j2'), post=post)

