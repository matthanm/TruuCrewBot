from MessageMonitor import MessageMonitor
from Server import Server
import threading
import time
import schedule
import requests

class ResponseHandler(threading.Thread):
	def __init__(self):
		super(ResponseHandler, self).__init__()
		self.monitors = []
		self.server = Server()
		self.isRunning = True
	def run(self):
		self.server.start()
		while self.isRunning:
			length = len(self.server.postQueue)
			for post in self.server.postQueue:
				for monitor in self.monitors:
					monitor.printIfMatch(post)
				self.server.postQueue.remove(post)
			time.sleep(5)
	def stop(self):
		self.server.stop()
		self.isRunning = False