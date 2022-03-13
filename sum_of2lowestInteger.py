import requests
from bs4 import BeautifulSoup

resp = requests.get('https://stepik.org/media/attachments/lesson/209723/5.html') # скачиваем файл
html = resp.text
soup = BeautifulSoup(html, 'html.parser') # делаем суп
print(soup.text)
print(sum([int(x) for x in soup.text.split() if x.isdigit()]))

