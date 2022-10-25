from collections import Counter
from bs4 import BeautifulSoup
import requests


# Найти наиболее часто встречающиеся строчки, находящиеся между тегами <code>

html = requests.get("https://stepik.org/media/attachments/lesson/209719/2.html")
#print(html.status_code)

between_code = []
soup = BeautifulSoup(html.content, "html.parser")
for code in soup.find_all('code'):
    between_code += code

print(Counter(between_code).most_common)