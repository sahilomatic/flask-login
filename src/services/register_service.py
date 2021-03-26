from models.user import User
from werkzeug.security import generate_password_hash,check_password_hash

class RegisterService:
    def register_user(self,username,password): 
        try:
            dao = User()
            dao.email = username
            dao.password = generate_password_hash(password)
            dao.save()
        except Exception as err:
            return str(err)