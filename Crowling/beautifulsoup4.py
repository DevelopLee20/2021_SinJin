from re import S
import requests
from bs4 import BeautifulSoup
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%84%A4%EC%9D%B4%EB%B2%84%EB%89%B4%EC%8A%A4"
req = requests.get(url)
print(req.text)
#soup = BeautifulSoup(req.text)
#print(req.text)
#with open("temp.html","w") as f:
#    f.write(req.text)
#print(soup.find_all({"class":"list_news"}))
##print(req.text.find('class="news_cluster"'))