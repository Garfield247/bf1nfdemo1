# -*- coding: utf-8 -*-
import json
from flask import Blueprint, render_template,jsonify,request
from app.models import *
from app.extensions import redis_cli
# from sqlalchemy import *
from app.utils import RedisCliKeys
from app.utils.bf1api import Bf1Api

main = Blueprint('main', __name__)

@main.route("/",methods=["POST"])
def hello_world():

    print(request.data)
    try:
        row = request.data.decode("utf-8")
        j = json.loads(row)
        botName = j.get("user")
        stateKey = RedisCliKeys.BOTSTATES.format(user=botName)
        redis_cli.set(stateKey,row)
        redis_cli.expire(stateKey,int(30))
        commandKey = RedisCliKeys.BOTCOMMANDS.format(user=botName)
        botCommand = redis_cli.get(commandKey)
        if botCommand:
            return botCommand
        else:
            return ""
    except Exception as err:
        print(err)
        return ""

@main.route('/')
def index():
    return render_template('/main/index.html')

@main.route('/join/<botName>/<gameID>')
def join(botName,gameID):

    command = '{"command":"join %s"}'%gameID 
    stateKey = RedisCliKeys.BOTSTATES.format(user=botName)
    if redis_cli.get(stateKey):
        commandKey = RedisCliKeys.BOTCOMMANDS.format(user=botName)
        redis_cli.set(commandKey,command)
        return "已添加命令"
    else:
        
        return "Bot未向主控注册或断开"

@main.route('/bots/',methods=["GET"])
def bot_list():
    stateBaskKey = RedisCliKeys.BOTSTATES.format(user="*")
    keys = redis_cli.keys(stateBaskKey)
    if len(keys) > 0:
        return json.dumps([json.loads(redis_cli.get(k)) for k in keys])
    return ""
        
@main.route('/leave/<botName>',methods=["GET"])
def leave(botName):
    stateKey = RedisCliKeys.BOTSTATES.format(user=botName)
    row = redis_cli.get(stateKey)
    if row:
        j = json.loads(row)
        session = j.get("sessionId")
        gameID = j.get("gameId")
        print(session,gameID)
        res = Bf1Api.leaveGame(session,gameID)
        print(res)
        return json.dumps(res)

    else:
        return "Bot未向主控注册或断开"
    return ""
