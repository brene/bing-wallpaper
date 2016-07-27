import requests
import subprocess

r = requests.get('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US')
body = r.json()
url = 'https://bing.com' + body['images'][0]['url']
subprocess.call(['wget', url, "-O", "wallpaper.jpg"])