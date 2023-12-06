from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog_posts_tags.sql")

post_repository = PostRepository(connection)
posts = post_repository.find_by_tag(1)
tags = post_repository.find_by_post(2)

print(posts, tags)
