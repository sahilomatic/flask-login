from mongoengine import Document, StringField
from werkzeug.security import generate_password_hash,check_password_hash

class User(Document):
    """
    TASK: Create a model for user with minimalistic
          information required for user authentication

    HINT: Do not store password as is.
    """

    username = StringField(db_field="username",required=True,max_length=30,primary_key = True)
    password = StringField(db_field="password",required=True)
    name = StringField()
    
    
if __name__ == "__main__":
    dao = User()
    dao.email = "sahil"
    dao.password = generate_password_hash("abcd")
    dao.save()
    
