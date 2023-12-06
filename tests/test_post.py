from lib.post import *
# id title
def test_post_constructs():
    post = Post(1, "Test Post")
    assert post.id == 1
    assert post.title == "Test Post"

def test_posts_format_nicely():
    post = Post(1, "Test Post")
    assert str(post) == "Post(1, Test Post)"

def test_posts_are_equal():
    post1 = Post(1, "Test Post")
    post2 = Post(1, "Test Post")
    assert post1 == post2