import logging
from flask import jsonify,request
import json
from services.user_service import UserService
from services.register_service import RegisterService
logger = logging.getLogger("default")


def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"

def login():
    username = None
    password = None
    if(request.method == "GET"):
        username = request.args.get('username')
        password = request.args.get('password')
    elif(request.method == "POST"):
        json_string = request.data
        obj = json.load(json_string)
        username = obj['username']
        password = obj['password']
    
    return jsonify(UserService().login_user(username,password))

def register():
    username = None
    password = None
    if(request.method == "GET"):
        username = request.args.get('username')
        password = request.args.get('password')
    elif(request.method == "POST"):
        json_string = request.data
        obj = json.load(json_string)
        username = obj['username']
        password = obj['password']
    
    return jsonify(RegisterService().register_user(username,password))
