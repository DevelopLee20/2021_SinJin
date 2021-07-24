import requests

def file_write(content):
    f = open("test.txt",'w',encoding='UTF-8')
    f.write(content)
    f.close()

def url_open(content):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={content}'
    crowling_content = requests.get(url)

    return crowling_content.text

# 완성 후 입력하게 변경
search = '테니스'
find_text = url_open(search)

crowling_text = url_open(find_text)
crowling_text.find('테니스')