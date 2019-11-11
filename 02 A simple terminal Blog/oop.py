from models.post import Post
from database import Database

Database.initialize()

post = Post(blog_id="123"
            ,title="Rich Dad Poor Dad"
            ,content="This is some content"
            ,author="Robert Kiyosaki")


post.save_to_mongo()





