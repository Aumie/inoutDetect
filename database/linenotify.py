import requests
import urllib.parse

LINE_ACCESS_TOKEN = "N7ae2jBeUl945TiVex0ngJXPlzjFVLxDyOSY0jb9D6s"
url = "https://notify-api.line.me/api/notify"
# https://notify-bot.line.me/my/
LINE_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded', "Authorization": "Bearer " + LINE_ACCESS_TOKEN}


def lineAlert(message):
    global url
    global LINE_HEADERS
    msg = urllib.parse.urlencode({"message": message})
    session = requests.Session()
    session.post(url, headers=LINE_HEADERS, data=msg)

