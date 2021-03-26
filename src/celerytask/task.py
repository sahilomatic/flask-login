from services.last_login import LastLoginLogic

import celery


@celery.task()
def last_login_task():
    dao = LastLoginLogic()
    try:
        user = dao.get_last_login_user()
        if(user is None):
            raise Exception("No information of last login user found.")
        
        dao.insert_last_user_info(user)
        return "Succesfuly updated."
    except Exception as err:
        return str(err)
    