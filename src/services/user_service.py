from models.user import User
import settings
from werkzeug.security import generate_password_hash,check_password_hash
import datetime

import jwt

class UserService(object):
    """
    service function for user related business logic
    """
    last_login = None
    
    def login_user(self,username,password):
        """
        TASKS: write the logic here for user login
               authenticate user credentials as per your
               schema and return the identifier user.

               raise appropriate errors wherever necessary
        """
        try:
            dao = User()
            user = dao.objects(username=username).first()
            if(user is None):
                raise Exception("Username not found in database.")
            last_login = user
            if(check_password_hash(user['password'], password)):
                
                jwt = self.encode_auth_token(username)
                
                return {'login':True, 'token':jwt}
            else:
                raise Exception("Password is incoreect.")
        except Exception as err:
            return str(err)
                
    
    
    
                      
                      
                      
    def encode_auth_token(self,username):
        """
        Generates the Auth Token
        
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': username
            }
            return jwt.encode(
                payload,
                settings.local_settings.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return {e}
        
    
    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        This function is kept static as it doesn't depend on UserService object.
        """
        try:
            payload = jwt.decode(auth_token, settings.local_settings.SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
           
        
        
        
        

        
