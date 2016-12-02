import threading
import time
import schedule
import requests

class AutoMessage(threading.Thread):
	def __init__(self, hour, minute, message):
		print("Creating new AutoMessage instance...")
		super(AutoMessage, self).__init__()
		self.hour = hour
		self.minute = minute
		self.message = message
		self.isRunning = True
	def run(self):
		if int(self.hour) >= 0 and int(self.hour) < 24 and int(self.minute) >= 0 and int(self.minute) < 60:
			printTime = self.hour.zfill(2) + ":" + self.minute.zfill(2)
			print("Setting '" + self.message + "' timer for " + printTime + "...")
			schedule.every().day.at(printTime).do(self.postMessage)
			print("'" + self.message + "' timer set.")
			while self.isRunning:
				schedule.run_pending()
				time.sleep(60)
		else:
			print("Invalid time, cannot instantiate new AutoMessage instance.")
	def stop(self):
		print("Disabling AutoMessage instance for '" + self.message + "'...")
		self.isRunning = False
	def postMessage(self):
		print("Executing print of '" + self.message + "'...")
		r = requests.post("https://api.groupme.com/v3/bots/post", data={"bot_id": "f5653fbe08bba8afa0c7db14da", "text": self.message})
		print(r.status_code, r.reason)