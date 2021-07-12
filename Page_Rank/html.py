import urllib.request

page = urllib.request.urlopen("https://www.naver.com/")
text = page.read().decode("utf-8")

print(text)
