from mongoengine import Document, StringField
from werkzeug.security import generate_password_hash,check_password_hash

class LastLogin(Document):
    

    username = StringField(db_field="username",required=True,max_length=30,primary_key = True)
    name = StringField()
    password = StringField(db_field="password",required=True)
    