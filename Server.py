from flask import Flask, request
import threading

class Server(threading.Thread):
	def __init__(self):
		super(Server, self).__init__()
		self.postQueue = []
		self.app = Flask(__name__)
		@self.app.route('/', methods=['POST'])
		def result():
			print("Received message.")
			self.postQueue.append(request.form['text'])
			return 'Received !'
	def run(self):
		print("Starting server...")
		self.app.run(threaded=True, host="0.0.0.0")
	def stop(self):
		print("Stopping server...")
