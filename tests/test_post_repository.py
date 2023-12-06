from lib.post_repository import *
from lib.post import *
from lib.tag import *

def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    tag = repository.find_by_tag(4)
    assert tag == [
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
    ]

def test_find_by_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    post = repository.find_by_post(1)
    assert post == [
        Tag(1, 'coding'),
    ]