import requests
import urllib.parse

LINE_ACCESS_TOKEN = "N7ae2jBeUl945TiVex0ngJXPlzjFVLxDyOSY0jb9D6s"
url = "https://notify-api.line.me/api/notify"
# https://notify-bot.line.me/my/
message = "test"
msg = urllib.parse.urlencode({"message": message})
LINE_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded', "Authorization": "Bearer " + LINE_ACCESS_TOKEN}
session = requests.Session()
a = session.post(url, headers=LINE_HEADERS, data=msg)
print(a.text)
