from lib.post import *
from lib.tag import *

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_by_tag(self, tag_id):
        rows = self._connection.execute(
            "SELECT * FROM posts " \
            "JOIN posts_tags ON posts_tags.post_id = posts.id " \
            "JOIN tags ON posts_tags.tag_id = tags.id " \
            "WHERE tags.id = %s", [tag_id])
        posts = []
        for row in rows:
            post = Post(row["post_id"], row["title"])
            posts.append(post)
        return posts

    def find_by_post(self, post_id):
        rows = self._connection.execute(
            "SELECT * FROM tags " \
            "JOIN posts_tags ON posts_tags.tag_id = tags.id " \
            "JOIN posts ON posts_tags.post_id = posts.id " \
            "WHERE posts.id = %s", [post_id])
        tags = []
        
        for row in rows:
            tag = Tag(row["tag_id"], row["name"])
            tags.append(tag)
        return tags
