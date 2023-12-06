from lib.tag import *

# id, name
def test_tag_constructs():
    tag = Tag(1, "Test Tag")
    assert tag.id == 1
    assert tag.name == "Test Tag"

def test_tags_format_nicely():
    tag = Tag(1, "Test Tag")
    assert str(tag) == "Tag(1, Test Tag)"

def test_tags_are_equal():
    tag1 = Tag(1, "Test Tag")
    tag2 = Tag(1, "Test Tag")
    assert tag1 == tag2