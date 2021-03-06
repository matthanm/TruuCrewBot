import threading
import datetime
import time
import schedule
import requests

class MessageMonitor():
    def __init__(self, expr, message):
        print("Creating new MessageMonitor instance...")
        super(MessageMonitor, self).__init__()
        self.expr = expr.split('.')
        self.message = message
    def printIfMatch(self, post):
        flag = True
        for expr in self.expr:
            if expr.lower() not in post.lower():
                flag = False
        if flag:
            time = datetime.datetime.now()
            finalMessage = self.message.replace("{now}", str(time))
            print("Executing print of '" + finalMessage + "'...")
            r = requests.post("https://api.groupme.com/v3/bots/post", data={"bot_id": "2dcdbc43412c876c1c4cf8f8b7", "text": finalMessage})
            print(r.status_code, r.reason)