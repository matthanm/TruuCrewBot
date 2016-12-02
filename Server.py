from flask import Flask, request
import json
import urllib.request
import threading

class Server(threading.Thread):
    def __init__(self):
        super(Server, self).__init__()
        self.postQueue = []
        self.app = Flask(__name__)
        @self.app.route("/", methods=["POST"])
        def result():
            print("Received message.")
            data = json.loads(request.data.decode("utf-8"))
            if data["sender_type"] != "bot":
                self.postQueue.append(data["text"])
            return "Response !"
    def run(self):
        print("Starting server...")
        self.app.run(threaded=True, host="0.0.0.0")
    def stop(self):
        print("Stopping server...")