import sqlite3
from datetime import datetime

from meier_app.models.post import Post
from meier_app.models.post_tag import PostTag
from meier_app.models.tag import Tag


def migrate(src, dest):
    try:
        conn = sqlite3.connect(src)
        c = conn.cursor()
        c.execute('''SELECT * from posts;''')
        posts_result = c.fetchall()

        c.execute('''SELECT * from tags;''')
        tags_result = c.fetchall()

        c.execute('''SELECT * from posts_tags;''')
        posts_tags_result = c.fetchall()

        conn.close()

        post_list = []
        for r in posts_result:
            id=r[0]
            title = r[2].encode('utf-8')
            slug = r[3].encode('utf-8')
            markdown = r[4].encode('utf-8')
            html = r[5].encode('utf-8')
            image = r[6]
            if r[9] and r[9] == 'published':
                status = 1
            else:
                status = 0
            created_at = r[14]
            updated_at = r[16]

            if r[20] and r[20] == 'public':
                visibility = 1
            else:
                visibility = 0

            post_list.append(Post(id=id,
                                  title=title,
                                  content=markdown,
                                  html=html,
                                  status=status,
                                  visibility=visibility,
                                  post_name=slug,
                                  in_date=datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S"),
                                  mo_date=datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S")))

        tag_list = []
        for r in tags_result:
            id = r[0]
            name = r[2].encode('utf-8')
            created_at = r[9]
            updated_at = r[11]
            tag = Tag(id=id, tag=name, in_date=datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S"), mo_date=datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S"))
            tag_list.append(tag)

        post_tag_list = []
        for r in posts_tags_result:
            id = r[0]
            post_id = r[1]
            tag_id = r[2]
            post_tag_list.append(PostTag(id=id, post_id=post_id, tag_id=tag_id))
        return post_list, tag_list, post_tag_list 
    except Exception as e:
        raise e

