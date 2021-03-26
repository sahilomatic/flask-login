from models.last_login import LastLogin
from services.user_service import UserService

class LastLoginLogic:
    def get_last_login_user(self):
        
            user = UserService.last_login
            return user
                
            
    
    def insert_last_user_info(self,user):
        try:
            dao = LastLogin()
            dao.email = user['username']
            dao.name = user['name']
            dao.password = user['password']
            dao.save()
        except Exception as err:
            return str(err)
        