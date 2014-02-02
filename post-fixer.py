import peewee as pw
from peewee import *
import json
import sys

access = json.load(open('access.json'))
khon = pw.MySQLDatabase("khon", user=access["user"], passwd=access["password"])
khon.connect()

class BaseModel(Model):
    class Meta:
        database = khon

class wp_posts(BaseModel):
    ID = BigIntegerField()
    post_author = BigIntegerField()
    post_date = DateTimeField()
    post_date_gmt = DateTimeField()
    post_content = TextField()
    post_title = TextField()
    post_category = IntegerField()
    post_excerpt = TextField()
    post_status = CharField(20)
    comment_status = CharField(20)
    ping_status = CharField(20)
    post_password = CharField(20)
    post_name = CharField(200)
    to_ping = TextField()
    pinged = TextField()
    post_modified = DateTimeField()
    post_modified_gmt = DateTimeField()
    post_content_filtered = TextField()
    post_parent = BigIntegerField()
    guid = CharField(255)
    menu_order = IntegerField()
    post_type = CharField(20)
    post_mime_type = CharField(100)
    comment_count = BigIntegerField()

def main():
    print sys.argv
    if (sys.argv[1] > 0):
      post_id = int(sys.argv[1])
    else:
      print "must supply post_id."
    post_ids = wp_posts.select()
    for post in post_ids:
        print post.ID

if __name__ == "__main__":
    main()
