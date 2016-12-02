from AutoMessage import AutoMessage
from ResponseHandler import ResponseHandler
from MessageMonitor import MessageMonitor

import threading
import sys
import requests
import time

def main():
	messages = []
	responseHandler = ResponseHandler()
	responseHandler.start()
	time.sleep(1)
	while True:
		### Enter arguements
		args = input("\nEnter a command: ").split(" ")

		### Create new bot function
		if args[0] == "enable":
			length = len(args)
			if length > 1:
				if args[1] == "automsg":
					if length >= 5 and args[2].isdigit() and args[3].isdigit():
						msg = ""
						for i in range(4, length):
							if i != 4:
								msg += " "
							msg += args[i]
						message = AutoMessage(args[2], args[3], msg)
						message.start()
						messages.append(message)
					else:
						print("Valid format: enable automsg [hour] [minute] [message]")
				elif args[1] == "monitor":
					if length >= 4:
						msg = ""
						for i in range(3, length):
							if i != 3:
								msg += " "
							msg += args[i]
						monitor = MessageMonitor(args[2], msg)
						responseHandler.monitors.append(monitor)
					else:
						print("Valid format: enable monitor [expression] [message]")
				else:
					print("Invalid enable option. Valid options are: automsg / monitor")
			else:
				print("Must enter something to enable. Valid options are: automsg / monitor")

		### Disable existing bot function
		elif args[0] == "disable":
			length = len(args)
			if length > 1:
				if args[1] == "automsg":
					if length >= 3:
						msg = ""
						for i in range(2, length):
							if i != 2:
								msg += " "
							msg += args[i]
						flag = False
						for message in messages:
							if message.message == msg:
								print("Found matching message.")
								flag = True
								message.stop()
								messages.remove(message)
								break
						if not flag:
							print("Message does not currently exist.")
					else:
						print("Valid format: disable automsg [message]")
				elif args[1] == "monitor":
					if length >= 3:
						msg = ""
						for i in range(2, length):
							if i != 2:
								msg += " "
							msg += args[i]
						flag = False
						for monitor in responseHandler.monitors:
							if monitor.message == msg:
								print("Found matching monitor.")
								flag = True
								responseHandler.monitors.remove(monitor)
								print("Disabling AutoMessage instance for '" + monitor.message + "'...")
								break
						if not flag:
							print("Monitor does not currently exist.")
					else:
						print("Valid format: disable monitor [message]")
				else:
					print("Invalid disable option. Valid options are: automsg / monitor")
			else:
				print("Must enter something to disable. Valid options are: automsg / monitor")

		### Manual print
		elif args[0] == "print":
			length = len(args)
			if length > 1:
				message = ""
				for arg in args[1:]:
					message += arg
				print("Executing print of '" + message + "'...")
				r = requests.post("https://api.groupme.com/v3/bots/post", data={"bot_id": "f5653fbe08bba8afa0c7db14da", "text": message})
				print(r.status_code, r.reason)
			else:
				print("You have to enter a message to print!")

		### Exit program
		elif args[0] == "exit":
			for message in messages:
				message.stop()
			responseHandler.stop()
			print("Turning off TruuCrewBot...")
			exit()

		### Invalid command
		else:
			print("Invalid command. Please try again...")

if __name__ == "__main__":
	main()