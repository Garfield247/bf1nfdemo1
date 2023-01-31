import requests
from uuid import uuid4


class Bf1Api:
    baseUrl = "https://sparta-gw-bf1.battlelog.com/jsonrpc/pc/api"
    headers = {
            "Content-Type": "application/json",
            "X-Gatewaysession": "77c34e1c-dfad-4394-ad50-b4ce7ee6e3a5",
            "Host": "sparta-gw.battlelog.com",
        }

    @classmethod
    def leaveGame(cls,session,gameId):
        data = {
            "jsonrpc":"2.0",
            "method":"Game.leaveGame",
            "params":{
                "game":"tunguska",
                "gameID":gameId,
            },
            "id":str(uuid4())
        }
        headers = cls.headers
        headers["X-Gatewaysession"] = session
        res = requests.post(url=cls.baseUrl,data=data,headers=headers,verify=False)
        return res.text
