import requests
r = requests.post("https://api.groupme.com/v3/bots/post", data={"bot_id": "2dcdbc43412c876c1c4cf8f8b7", "text": "dawgs"})
print(r.status_code, r.reason)
print(r.text[:300] + "...")